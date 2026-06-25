---
title: Rendering the Sky, Sunsets, and Planets
source: https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/
author:
- '[[ibobev]]'
published: '2026-05-12'
created: '2026-05-13'
description: 'Article URL: https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/
  Comments URL: https://news.ycombinator.com/item?id=48107997 Points: 495 # Comments:
  39'
tags:
- clippings
id: e0313ac9ee5cabe1
source_type: community_discussion
tldr: 本文详述了通过屏幕空间后处理着色器，结合 Rayleigh 散射、Mie 散射和臭氧吸收实现逼真天空/日落渲染的技术方案。
objective_summary: Maxime Heckel 撰写了一篇技术博客，从头实现基于 raymarching 的大气散射着色器。文章逐步构建了 Rayleigh
  散射（蓝天）、Mie 散射（尘埃雾状辉光）和臭氧吸收（暮色加深）三种光学模型，并加入光源方向步进（light marching）以实现日落效果，最终讨论了
event_type: application_landing
epistemic_status: verified_fact
entities:
  companies: []
  technologies:
  - Rayleigh scattering
  - Mie scattering
  - Ozone absorption
  - Raymarching
  - Beer's Law
  - light marching
  - LUT (Look-Up Table)
  - ACES film tone mapping
  key_people:
  - Maxime Heckel
  - Sebastian Hillaire
key_logic_flow:
- 使用 raymarching 从相机位置向场景投射射线，逐步采样大气密度以计算光学深度和透射率。
- Rayleigh 散射模型通过瑞利密度函数和相位函数描述蓝光在空气中散射强烈、红光散射弱的物理机制，是天空呈现蓝色的主要原因。
- Mie 散射模型模拟尘埃和气溶胶对光的散射，产生太阳周围的白雾状辉光，尤其在太阳接近地平线时更明显。
- 臭氧吸收模型不散射光，仅吸收上层大气中特定波段的光，使地平线和日落时分天空颜色更深、偏紫红。
- 引入光源方向步进，在每个采样点向太阳方向做二次步进，计算光线到达该点前的大气衰减，实现真实的日出/日落色彩变化。
- 最后讨论 Sebastian Hillaire 基于 LUT（预计算查找表）的优化方法，以减少运行时计算开销、提升性能。
extract_result: partial
---

# On Rendering the Sky, Sunsets, and Planets

There’s this photo that’s been sitting on my inspiration board for a while, of the space shuttle Endeavour, suspended in space in low Earth orbit at sunset. It shows Earth’s upper atmosphere as a backdrop, featuring beautiful, colorful layers ranging from dark orange to blue before fading away into the deep black of space. Not only is that gradient of color aesthetically pleasing, but the phenomenon behind those colors, **atmospheric scattering**, is even more of an interesting topic once you start looking into how it works and how to reproduce it.

I wanted to build my own version of this effect with shaders, rendering the sky’s distinctive blue color and realistic sunsets and sunrises directly in the browser. The goal was to get as close as I could to that photo, while also moving toward the kind of atmospheric rendering often seen in games and other shader-based media.

Here’s a compilation of what came out of this month-long journey, all running in real time:

I didn’t originally plan on writing about this subject, but the enthusiasm around the recent Artemis II mission, combined with my own interest in all things space, made it feel worth exploring in depth. It also felt like the perfect opportunity to build an interactive experience that could make the topic more accessible.
In this write-up, we’ll see **how to implement an atmospheric scattering shader post-processing effect step-by-step**, starting with the implementation of the different building blocks (raymarching, Rayleigh and Mie scattering, as well as ozone absorption) to render **a realistic sky dome**, and then adapt the result to render it as **an atmospheric shell around a planet**.
Finally, we'll look into Sebastian Hillaire’s LUT-based approach for a more performant result, or at least my *attempt* at implementing it, as this was very much the *stepping outside of my comfort zone* phase for this project.

You may have, at some point or another, tried to slap a blue gradient background behind some of your work in an attempt to give it a more "atmospheric" look and call it a day, but quickly noticed doing so never feels quite right 1.

For a more true to life implementation, we must treat the sky and its color as **the result of light interacting with air and its constituents**, while taking into account several variables, such the altitude of the observer, the amount of dust, the time of day, etc, all of that **in a volume**.

With that established, our goal for this first part is to use this as guiding principle to lay the foundation for our atmosphere shader, and get to a result that feels almost indistinguishable from a real sky, at any time of the day.

Much like how we’d approach volumetric clouds or volumetric light, one easy way to sample the atmosphere is through **raymarching**. We can cast rays from the camera’s position into the scene and step through the transparent medium to answer the two following questions:

- How much light survives traveling through the atmosphere? This is the
**transmittance**term. - How much light is redirected toward the camera at each sample? Also known as
**scattering**.

To answer the first one, we need to accumulate the atmospheric density encountered along the ray to obtain what is known as the *optical depth*. We will model this using the **Rayleigh density function**, which tells us how much *"air"* there is at a given altitude `h`

. This is important to take into account that the atmosphere gets thinner as altitude increases.

Sampling Rayleigh density and accumulating optical depth

1const float RAYLEIGH_SCALE_HEIGHT = 8.0; // km2const float ATMOSPHERE_HEIGHT = 100.0; // km - Karman line3const float VIEW_DISTANCE = 200.0; // km4const int PRIMARY_STEPS = 24;5const vec3 SUN_DIRECTION = normalize(vec3(0.0, 1.0, 1.0));67float rayleighDensity(float h) {8return exp(-max(h, 0.0) / RAYLEIGH_SCALE_HEIGHT);9}1011void main() {12vec2 p = vUv * 2.0 - 1.0;1314vec3 color = vec3(0.0);15vec3 viewDir = normalize(vec3(p.x, p.y, 1.0));16vec3 skyDir = normalize(vec3(viewDir.x, max(viewDir.y, 0.0), viewDir.z));1718float stepSize = VIEW_DISTANCE / float(PRIMARY_STEPS);19float viewOpticalDepth = 0.0;2021for (int i = 0; i < PRIMARY_STEPS; i++) {22float t = (float(i) + 0.5) * stepSize;23float h = t * skyDir.y;2425if (h < 0.0) break;26if (h > ATMOSPHERE_HEIGHT) break;2728float dR = rayleighDensity(h);29viewOpticalDepth += dR * stepSize;3031// ...32}3334//...3536color = ACESFilm(color);3738fragColor = vec4(color, 1.0);39}

Then, from the optical depth, we can compute the **transmittance** `T`

at a given point along the ray: the fraction of light that survives while traveling through the atmosphere.

`T=1.0`

means that there is no loss of light.`T=0.0`

means that the light is totally extinguished.

If you’ve read my article on volumetric clouds 2, we’re using a formula that may look familiar for this: **Beer's Law**:

Computing transmittance

1//...23float dR = rayleighDensity(h);4viewOpticalDepth += dR * stepSize;56vec3 transmittance = exp(-rayleighBeta * viewOpticalDepth);7scattering += dR * transmittance * stepSize;89//...

With this in place, we can now describe how light is *attenuated* as it travels through the atmosphere. However, density and transmittance only tell us how much light is available to scatter, not how that light is distributed toward the viewer. For that, we need to account for the angle between the incoming sunlight and the view ray, which is what the **Rayleigh phase function** models.

Rayleigh phase function

1//...23// We consider the sun constant at its zenith here4const vec3 SUN_DIRECTION = normalize(vec3(0.0, 1.0, 1.0));56float rayleighPhase(float mu) {7return 3.0 / (16.0 * PI) * (1.0 + mu * mu);8}910//...11void main() {12//...13float phase = rayleighPhase(dot(skyDir, SUN_DIRECTION));1415// Raymarching loop1617scattering *= SUN_INTENSITY * phase * rayleighBeta;1819float horizon = smoothstep(-0.12, 0.05, skyDir.y);20vec3 color = mix(SPACE_COLOR, scattering, horizon);21color = ACESFilm(color);2223fragColor = vec4(color, 1.0);24}

Putting all this together, we can have a somewhat accurate representation of how much scattered light accumulates along a given ray at any given altitude. The widget below represents the process we just described, showing you:

- The sample steps along a single ray
- The resulting pixel color obtained from this process (an approximation)

As you can see, we’re accumulating shades of blue at lower altitude! This is mostly due to the Rayleigh scattering coefficient’s value:

- Red scatters very little
- Green a bit more
- Blue the most

Since shorter wavelengths scatter more strongly, more blue light is redirected toward the viewer, thus resulting in the sky appearing *blue* during daytime.

If we expand this idea into a full-on fragment shader, going from a single ray to one ray per pixel, we can render a realistic sky, as demonstrated below:

This raymarching process yields a beautiful **blue sky**, with a lighter white haze towards the horizon as rays travel through more atmosphere there, and deeper, darker blue colors as the altitude increases and the atmosphere gets thinner.

While Rayleigh scattering alone yields a decent result, there are still additional atmospheric effects that we can take into account to make our sky rendering closer to reality:

**Mie Scattering**, which describes the interaction of light with larger particles in the atmosphere, like dust or aerosols. It has a density function to account for the amount of material in the medium, as well as a phase function, which, like its Rayleigh counterpart, describes how the light gets redistributed in different directions.**Ozone absorption**, which models how ozone absorbs part of the light passing through the upper atmosphere. This one does not scatter light; it only removes some wavelengths along the path. Its main contribution is to*shift and deepen the sky’s color*, especially near the horizon and during sunsets or twilight.

The first one can be modeled with the following two functions:

Mie density and phase function

1float miePhase(float mu) {2float gg = MIE_G * MIE_G;3float num = 3.0 * (1.0 - gg) * (1.0 + mu * mu);4float den = 8.0 * PI * (2.0 + gg) * pow(max(1.0 + gg - 2.0 * MIE_G * mu, 1e-4), 1.5);5return num / den;6}78float mieDensity(float h) {9return exp(-max(h, 0.0) / MIE_SCALE_HEIGHT);10}

To get the updated scattering term that takes Mie scattering and Ozone into account, we simply add it to the current implementation of our sky shader on top of the Rayleigh density and phase function:

Rayleigh, Mie, and Ozone scattering terms

1float viewODR = 0.0;2float viewODM = 0.0;3float viewODO = 0.0;45vec3 sumR = vec3(0.0);6vec3 sumM = vec3(0.0);7vec3 sumO = vec3(0.0);89for (int i = 0; i < PRIMARY_STEPS; i++) {10float t = (float(i) + 0.5) * stepSize;11float h = uObserverAltitude + t * skyDir.y;1213if (h < 0.0) break;14if (h > ATMOSPHERE_HEIGHT) break;1516float dR = rayleighDensity(h);17float dM = mieDensity(h);18float dO = ozoneDensity(h);1920viewODR += dR * stepSize;21viewODM += dM * stepSize;22viewODO += dO * stepSize;2324vec3 tau = BETA_R * viewODR25+ BETA_M_EXT * viewODM26+ BETA_OZONE_ABS * viewODO;27vec3 transmittance = exp(-tau);2829sumR += dR * transmittance * stepSize;30sumM += dM * transmittance * stepSize;31sumO += dO * transmittance * stepSize;32}3334vec3 scattering = SUN_INTENSITY * (35phaseR * BETA_R * sumR +36phaseM * BETA_M_SCATTER * sumM +37BETA_OZONE_SCATTER * sumO38);3940float horizon = smoothstep(-0.12, 0.05, skyDir.y);41vec3 color = mix(SPACE_COLOR, scattering, horizon);42color = ACESFilm(color);4344fragColor = vec4(color, 1.0);

The widget below showcases the result of integrating both of those new terms into our sky shader:

As you can see, this version yields both:

- A more natural “sky blue” color, thanks to our ozone absorption

- A hazy glow around the location of our sun, and even more so visible when the sun is close to the horizon

At this point, we have a decent sky fragment shader capable of rendering a natural color for any altitude and taking into account a diverse set of transmittance models (Mie, Rayleigh, and Ozone). That still leaves us with lighting to work on.

You may have noticed in the previous widget that moving the sun close to the horizon only results in a *white, hazy glow*, without any light attenuation or a sunset/sunrise effect. This is expected, as our current raymarching loop only accounts for light being attenuated along the view ray, from the camera to each sample. It does not yet account for how much sunlight is lost while traveling through the atmosphere before reaching that sample point.
As we did for in related past articles, we need to introduce, for any given sample point alongside our ray, a standalone nested loop to light-march in the direction of the light source and sample the *transmittance* along that path.

In our previous implementation, the optical depth was only computed along the ray through `viewODR`

, `viewODM`

, and `viewODO`

. For this updated version, we will:

- Add a
`sunOD`

value that carries the amount of optical depth accumulated along the path between the sample point and the sun.

1vec3 lightMarch(float start, float sunY) {2float denom = max(sunY + 0.15, 0.04);3float maxDist = (ATMOSPHERE_HEIGHT - start) / denom;4float stepSize = max(maxDist, 0.0) / float(LIGHTMARCH_STEPS);5float odR = 0.0;6float odM = 0.0;7float odO = 0.0;89for (int i = 0; i < int(LIGHTMARCH_STEPS); i++) {10float t = (float(i) + 0.5) * stepSize;11float h = start + t * sunY;12if (h < 0.0 || h > ATMOSPHERE_HEIGHT) {13continue;14}1516odR += rayleighDensity(h) * stepSize;17if (uMieEnabled) odM += mieDensity(h) * stepSize;18if (uOzoneEnabled) odO += ozoneDensity(h) * stepSize;19}2021return vec3(odR, odM, odO);22}

- Sum it with each individual optical depth we introduced earlier in our
`tau`

variable.

1float dR = rayleighDensity(h);2float dM = mieDensity(h);3float dO = ozoneDensity(h);45viewODR += dR * stepSize;6viewODM += dM * stepSize;7viewODO += dO * stepSize;89vec3 sunOD = uSunAngle > 0.0 && uSunAngle < PI ? lightMarch(h, sunDirection.y) : vec3(1000.0);10vec3 tau = BETA_R * (viewODR + sunOD.x)11+ BETA_M_EXT * (viewODM + sunOD.y)12+ BETA_OZONE_ABS * (viewODO + sunOD.z);13vec3 transmittance = exp(-tau);

With this in place, we now have the ability to render our sky under any light condition; sunsets, sunrises, zenith, and anything in between.

I invite you to take a little break and play with the widget above to appreciate the different colors of the sky our shader can now yield through this now fully implemented sky model. Notice how:

- The blue of the sky changes throughout the day, represented here by the
`sun angle`

uniform, and how the light nicely blends with the horizon at sunset and sunrise, thanks to Mie scattering. - The ozone gives our sky a nice
*purple-ish*tone when the sun is low.

The shader we just built in this first section checks a lot of boxes, but we have in place right now is just a mere flat background. If we were to use it in a React Three Fiber scene in its current state, we would simply have a nice backdrop for our scenes and not much more beyond that.

In this section, we will turn our flat shader into a proper **post-processing effect**, allowing us to render the atmosphere as:

*a volume*and account for scene depth along the way by reconstructing world-space coordinates from`screenUV`

coordinates.*a shell around a planet mesh*.

To apply atmospheric scattering to a scene, we aren't just drawing a sky; we need to fill the space between the camera and the different objects rendered on screen. Lucky us, we already partially did that work in part one: we have all the density data necessary to compute the *stuff* in the volume that is our 3D scene. The only thing needed here is to:

- Create a post-processing effect that can render our sky shader.
- Get the depth buffer of our scene and the camera’s
`projectionMatrixInverse`

,`matrixWorld`

, and`position`

, to pass them as uniforms of the effect. - Reconstruct 3D rays from our camera through each pixel of our effect by converting screen space coordinates into world space coordinates with the following function:

getWorldPosition function

1vec3 getWorldPosition(vec2 uv, float depth) {2float clipZ = depth * 2.0 - 1.0;3vec2 ndc = uv * 2.0 - 1.0;4vec4 clip = vec4(ndc, clipZ, 1.0);56vec4 view = projectionMatrixInverse * clip;7vec4 world = viewMatrixInverse * view;89return world.xyz / world.w;10}

Now that we know how to obtain the `worldPosition`

of the current pixel, we can:

- Set our
`rayOrigin`

to the position of the camera. - Set our
`rayDir`

to the normalized difference between the worldPosition and our rayOrigin

Doing this will ensure our raymarch loop now marches along a **3D ray**.

Sampling along a 3D ray

1float depth = readDepth(depthBuffer, uv);2vec3 rayOrigin = uCameraPosition;3vec3 worldPosition = getWorldPosition(uv, depth);4vec3 rayDir = normalize(worldPosition - rayOrigin);

The last thing we need to do now is to have our raymarching take into account any geometry in the scene. To do so, we will use the depth buffer of our scene to define our raymarch `stepSize`

rather than using a constant so that we can space our sample points to fit the ray we are currently marching along.

1float depth = readDepth(depthBuffer, uv);2vec3 rayOrigin = uCameraPosition;3vec3 worldPosition = getWorldPosition(uv, depth);4vec3 rayDir = normalize(worldPosition - rayOrigin);56float sceneDepth = depthToRayDistance(uv, depth);78// This is just an arbitrary value to sample "far enough"9// within our sky dome10float SKY_MARCH_DISTANCE_MULTIPLIER = 8.0;1112bool isBackground = depth >= 1.0 - 1e-7;1314// Fallback for "sky pixels" i.e. background pixels.15// We cap how far we will march16if (isBackground) {17sceneDepth = atmosphereHeight * SKY_MARCH_DISTANCE_MULTIPLIER;18}1920float rayStart = 0.0;21float rayEnd = max(sceneDepth, 0.0);22float tGround = 1e9;2324if (rayDir.y < -1e-5) {25tGround = observerAltitude / max(-rayDir.y, 1e-4);26rayEnd = min(rayEnd, tGround);27}2829float stepSize = (rayEnd - rayStart) / float(PRIMARY_STEPS);

- This lets us be very accurate in our sampling for rays that hit nearby objects or the ground: the
`stepSize`

will be small. - We can afford to be a bit less precise for rays that travel further, since those cover larger distances and we distribute an equivalent amount of sample points along them.

The playground below renders the same shader we put together earlier, but this time as a post-processing effect, letting us render Atmospheric Scattering throughout the scene’s volume, taking its geometries into account, with our sky shader as a backdrop.

Notice how:

- The closer objects are to the camera, the clearer they will appear.
- The further objects are from the camera, the more they will fade away.

With that implemented, we can start providing a more realistic ambient sky to any scene that would need it, and also have some fun with some *silly interactions* like this one below, implemented with a `Raycaster`

:

atmosphere post-processing effect now with draggable celestial objects https://t.co/xejzC5SWuc https://t.co/U342icnvxz

We’re finally reaching the part you probably came here for in the first place: **rendering a realistic atmosphere around planets!** Luckily, with everything we built up to this point, we only have two steps missing to achieve that:

- Switch to a logarithmic depth buffer to handle larger scales.
- Define where the atmosphere starts and where it stops along any given ray to define its shape, which, as you can guess, will be a sphere.

Since we’re working at a planetary scale in this section, we can expect a lot of “depth fighting” when viewing our planet from afar, as it is hard for our shader to differentiate the depth between the atmosphere and planet shell from a large distance (the atmosphere height being only a few km). We need to adjust both the way our depth buffer is defined in our React Three Fiber scene and how it’s read. To do so, we set `logarithmicDepthBuffer`

to `true`

in the `gl`

prop of our `Canvas`

component that wraps the entire scene definition:

Enabling logarithmic depth buffer for our scene

1<Canvas2shadows3gl={{4alpha: true,5logarithmicDepthBuffer: true,6}}7>8{/* Scene */}9</Canvas>

Then, in our shader, we redefine our sceneDepth as follows to convert the lograithmic depth buffer received by the post-processing effect, and convert it back into a distance along the ray.

Updated getWorldPosition function

1float logDepthToViewZ(float depth) {2float d = pow(2.0, depth * log2(cameraFar + 1.0)) - 1.0;3return -d;4}56float logDepthToRayDistance(vec2 uv, float depth) {7float viewZ = logDepthToViewZ(depth);8vec2 ndc = uv * 2.0 - 1.0;9vec4 clipAtZ1 = vec4(ndc, -1.0, 1.0);10vec4 viewAtZ1 = projectionMatrixInverse * clipAtZ1;11viewAtZ1 /= viewAtZ1.w;12vec3 viewRayDir = normalize(viewAtZ1.xyz);13float cosTheta = max(-viewRayDir.z, 1e-5);14return (-viewZ) / cosTheta;15}1617vec3 getWorldPosition(vec2 uv, float depth) {18float viewZ = logDepthToViewZ(depth);19vec2 ndc = uv * 2.0 - 1.0;20vec4 clipAtZ1 = vec4(ndc, -1.0, 1.0);21vec4 viewAtZ1 = projectionMatrixInverse * clipAtZ1;22viewAtZ1 /= viewAtZ1.w;23vec3 viewPos = viewAtZ1.xyz * (viewZ / viewAtZ1.z);24vec4 world = viewMatrixInverse * vec4(viewPos, 1.0);25return world.xyz;26}

For the second point, we will use **a ray-sphere intersection test** to find where our view ray enters and exits the *atmospheric sphere*. Once we have those two points, we can limit our raymarching loop to that segment without wasting samples outside the atmosphere.

However, just doing a single test is not enough. We also want to model our planet as a sphere mesh surrounded by a slightly larger atmosphere sphere, and thus, we will need to perform the same test against the planet itself. If the ray hits the ground before it exits the atmosphere, we use that ground intersection as the end of our raymarching segment.

Using ray-sphere intersection points in our raymarching loop

1vec3 planetCenter = vec3(0.0);23vec2 atmosphereHit = raySphereIntersect(4rayOrigin,5rayDir,6planetCenter,7atmosphereRadius8);910vec2 planetHit = raySphereIntersect(11rayOrigin,12rayDir,13planetCenter,14planetRadius15);1617// Only raymarch when we intersect the atmosphere shell at least once18if (atmosphereHit.x > 0.0 || atmosphereHit.y > 0.0) {19float atmosphereNear = max(atmosphereHit.x, 0.0);20float atmosphereFar = atmosphereHit.y;2122// If the ray hits the planet, stop marching at the ground.23if (planetHit.x > 0.0) {24atmosphereFar = min(atmosphereFar, planetHit.x);25} else {26// Otherwise, stop at the closest scene geometry sampled from the depth buffer.27atmosphereFar = min(atmosphereFar, sceneDepth);28}2930// Only compute scattering when the ray travels through a valid atmosphere segment.31if (atmosphereFar > atmosphereNear) {32// Compute scattering here33}34}

One additional thing we need to adapt is the end of our raymarching segment to handle objects within the scene. The atmosphere may stop for two different reasons:

- it can hit the planet surface
`planetHit.x > 0.0`

- it can hit another scene object before reaching the ground.

1// If the ray hits the planet, stop marching at the ground.2if (planetHit.x > 0.0) {3atmosphereFar = min(atmosphereFar, planetHit.x);4// However, another mesh may be rendered in front of the ground.5// In that case, stop the atmosphere at the scene depth instead.6if (sceneDepth < planetHit.x - 2.0) {7atmosphereFar = min(atmosphereFar, sceneDepth);8}9} else {10// If the ray does not hit the ground, the atmosphere segment can11// continue until we exits the atmosphere or reach a scene geometry.12atmosphereFar = min(atmosphereFar, sceneDepth);13}

In both cases, we want to stop marching at the closest relevant object.

Notice how, without this logic, the surface of the planet will appear *in front* of our object.

With those two parts now in code, we have a full implementation of atmospheric scattering as a post-processing effect and can render atmospheres around planets. The scene below renders a simple “Sun - Earth system” in React Three Fiber, with our custom effect in place. I invite you to take some time to adjust the position of the sun, zoom out, and enjoy the sky colors this shader can yield from different angles, from ground to orbit.

The effect you can see in this demo is the same one I used to take the photos for the posters I posted in early April to announce this article:

outline for my upcoming, and very much on theme, article on atmospheric scattering felt inspired and made posters with photos of actual renders made with the techniques you’ll learn in it :) very excited for this one https://t.co/wSjdQPyoI0

This is a little *bonus* section where I’d like us to answer the question: *how can we handle large celestial objects blocking the sun?* We now have a decent understanding of what’s at play in this atmospheric scattering shader when it comes to lighting, and adding this extra test is relatively easy.

We can add, after our lightMarch function, a function call that would return the`sunVisibility`

ranging from `[0, 1]`

and multiply the transmittance by this value. The function itself could be as easy as doing a dot product between:

- The direction between our current sampling point and the moon.
- The direction between our current sampling point and the sun.

If they were to match closely, i.e., close to `1.0`

, that means the moon would be obstructing the sun, and vice versa; if they were orthogonal, close to `0.0`

, there would be no obstruction. However, this doesn’t take into account the size and scale of the object in the scene.

We need a function that can handle the three cases described in the diagram above:

- When the moon is not obstructing the sun.
- When it is, but is larger or close to the size of the sun from the camera’s POV.
- When it is, but fits within the radius of the sun from the camera’s POV.

sunVisibility function

1float sunVisibility(vec3 point) {2vec3 sunDir = normalize(sunDirection);3vec3 toMoon = moonPosition - point;4float moonDist = length(toMoon);5vec3 moonDir = normalize(toMoon);67if (moonDist <= 1e-5) {8return 1.0;9}1011// Compare the apparent positions and sizes of the sun and moon in the sky.12float angularSep = acos(clamp(dot(sunDir, moonDir), -1.0, 1.0));13float sunAngularRadius = SUN_RADIUS / SUN_DISTANCE;14float moonAngularRadius = moonRadius / moonDist;15float outerEdge = sunAngularRadius + moonAngularRadius;1617// No overlap between the sun and moon disks: full sunlight.18if (dot(sunDir, moonDir) < 0.9) {19return 1.0;20}2122// The moon appears larger than the sun, so it can fully cover it near the center.23if (moonAngularRadius >= sunAngularRadius) {24float innerEdge = moonAngularRadius - sunAngularRadius;25return max(0.075, smoothstep(innerEdge, outerEdge, angularSep));26}2728float innerEdge = sunAngularRadius - moonAngularRadius;29float minVisibility = clamp(301.0 - (moonAngularRadius * moonAngularRadius) / (sunAngularRadius * sunAngularRadius),310.0,321.033);3435// Partial overlap: smoothly fade between the minimum and full sunlight.36return mix(minVisibility, 1.0, smoothstep(innerEdge, outerEdge, angularSep));37}

Here, `float angularSep = acos(clamp(dot(sunDir, moonDir), -1.0, 1.0))`

represents the angular separation between the sun and moon directions.

`dot(sunDir, moonDir)`

represents the alignment between both directions.`acos`

converts it back to an angle.

We can then use this value to compare it with the different angular thresholds `outerEdge`

and `innerEdge`

, representing, respectively, the angles at which the two discs start touching externally / internally.

The demo below implements this `sunVisibility`

function on top of our previous example, and also adds a moon mesh to our system. Try to align the moon with the sun, and notice how our Atmospheric Scattering shader properly handles the lack of light in those cases.

Another *bonus* section! It’s your lucky day! The model we’ve been using throughout this article to simulate atmospheric density and scattering is mostly governed by a handful of constants:

- The radius of the planet and atmosphere
`RayleighScaleHeight`

and`RayleighBeta`

.`MieScaleHeight`

,`MieBeta`

,`mieBetaExt`

, and`mieG`

`OzoneHeight`

and`OzoneWidth`


These are the main knobs that make our rendered atmosphere look the way it does. Thus, by tweaking them to the right set of values, we could, in theory, approach a martian atmosphere or even other planets'. Below is the set of values I set for Mars:

1// These values are only approximative23const Mars = {4planetRadius: 3390,5atmosphereRadius: 3500, // ~110 km thick6rayleighScaleHeight: 11.1,7rayleighBeta: new THREE.Vector3(0.019, 0.013, 0.0057),8mieScaleHeight: 1.5,9mieBeta: 0.04,10mieBetaExt: 0.044,11mieG: 0.65,12ozoneCenterHeight: 0.0,13ozoneWidth: 1.0,14ozoneBetaAbs: new THREE.Vector3(0.0, 0.0, 0.0),15sunIntensity: 15.0,16planetSurfaceColor: '#8B4513',17};

Just replacing our constants with these gives us a more dusty, orangy atmosphere. Even better, we get Mars' distinctive blue hue at sunset! Below are a couple of screenshots I took while working on this. You can try plugging those values into the previous demo to see the result by yourself.

The resulting shader we’ve built, albeit intuitive and able to render atmosphere at small and large scales, is unfortunately quite expensive to run:

- We have a large amount of
`PRIMARY_STEPS`

in our raymarching loop. - We have a nested loop for lightmarching.
- We perform all the math at full screen resolution.

Alongside tackling those drawbacks, I also wanted to study *how the pros were doing it* when I reached this point in my exploration of atmospheric scattering. Sebastian Hillaire proposed in his paper titled A Scalable and Production Ready Sky and Atmosphere Rendering Technique, a method to render atmosphere based on **Look Up Tables** (LUTs), i.e. textures that can hold expensive scattering calculations, so the final render samples and composes those precomputed textures.

In this part, we will look into the respective implementations of:

**Transmittance LUT**, which stores the amount of light that survives as it travels through the atmosphere.**Sky-view LUT**, which stores the resulting sky color for a given camera position**Aerial Perspective LUT**, which stores the atmospheric haze/fog between the camera and visible scene geometries, including the amount of light added by scattering and its effect on the scene’s colors.

In our original shader, every sample point calls the `lightmarch`

function to get the amount of light from our sun that reaches it, which, as you may guess, is quite expensive. The goal of this LUT is to store that data beforehand, preferably at a low resolution, so we can then load it into subsequent LUTs whenever we need that light data.

My implementation for this LUT, and any that follows, consists of:

- Define a dedicated Frame Buffer Object at a specific resolution. For this one in particular, I picked
`250 x 64`

. - Define a material with a custom shader that will hold the logic to generate our LUT data.
- Apply it to a full-screen quad in a dedicated scene, in this case,
`transmittanceLUTScene`

. - Render the scene, and pass the resulting texture as a uniform to downstream LUTs.

It may seem a bit convoluted, but as said before, ideally, you’d use WebGPU and compute shaders for this and thus not need those FBOs.

For the tramittance, we’re extracting the expensive lightmarch loop into its own pass by putting it in the `transmittanceLUTFragmentShader`

. The code below is what I used to generate my texture:

Transmittance LUT

1void main() {2float mu = mix(-1.0, 1.0, vUv.x);34float radius = mix(planetRadius, atmosphereRadius, vUv.y);5vec3 rayOrigin = vec3(0.0, radius, 0.0);6float sinTheta = sqrt(max(1.0 - mu * mu, 0.0));7vec3 rayDir = normalize(vec3(sinTheta, mu, 0.0));89vec2 atmosphereHit = raySphereIntersect(10rayOrigin,11rayDir,12vec3(0.0),13atmosphereRadius14);1516vec2 planetHit = raySphereIntersect(17rayOrigin,18rayDir,19vec3(0.0),20planetRadius21);2223float rayLength = atmosphereHit.y;2425if (rayLength <= 0.0) {26gl_FragColor = vec4(1.0);27return;28}2930if (planetHit.x > 0.0) {31gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);32return;33}3435float stepSize = rayLength / float(TRANSMITTANCE_STEPS);36float rayleighOD = 0.0;37float mieOD = 0.0;38float ozoneOD = 0.0;3940for (int i = 0; i < TRANSMITTANCE_STEPS; i++) {41float t = (float(i) + 0.5) * stepSize;42vec3 samplePoint = rayOrigin + rayDir * t;43rayleighOD += rayleighDensity(samplePoint) * stepSize;44mieOD += mieDensity(samplePoint) * stepSize;45ozoneOD += ozoneDensity(samplePoint) * stepSize;46}4748vec3 tau =49rayleighBeta * rayleighOD +50mieBetaExt * mieOD +51ozoneBetaAbs * ozoneOD;5253gl_FragColor = vec4(exp(-tau), 1.0);54}

- For each pixel, we ray march from
`vec3(0.0, radius, 0.0)`

, which grows between`planetRadius`

and`atmosphereRadius`

along the`vUv.y`

coordinate. - The direction
`rayDir`

defines the light direction for any given pixel of our LUT, which varies between`mu = -1`

, i.e., a downward direction toward the planet’s surface,`rayDir = vec3(0.0, -1.0, 0.0)`

, and`mu = 1`

, a upward direction toward space,`rayDir = vec3 (0.0, 1.0, 0.0)`

. When`mu = 0`

,`rayDir = vec3(1.0, 0.0, 0.0)`

meaning the light travels horizonally, grazing the atmosphere. - We use the same
`raySphereIntersect`

and atmospheric scattering functions introduced earlier.

This results in the following transmittance LUT texture:

Here’s how you can interpret this texture:

**The x-axis represents the angle of the light**. On the left side, we have light looking straight down towards the ground, hence the dark colors. The right side, on the other hand, represents light looking straight up.**The y-axis represents the altitude**. The bottom of the image is the ground / sea level, while the top is the edge of our atmosphere.- Pure white represents a transmittance of 100% where light has a clear path.
- Black/colored areas represent the ground/the part where the air is at its thickest, especially near the ground where some of the light is extinct.

Subsequent LUTs can now answer the question of *"how much light survives at a given angle and altitude through our atmosphere"* very quickly by just *looking up* that value in this texture.

These two LUTs leverage the transmittance data we just computed in its respective texture and answer two complementary questions:

- If I look in a specific direction from the ground up, what color is the sky?
**Sky Color** - How much atmosphere is between my current position and any object in the scene?
**Atmospheric Fog**

Combining both those LUTs will give us the full atmospheric scattering effect. The former handles far-field color while the latter calculates near-field haze. Using a similar process involving FBO and off-screen scenes, we can define distinct shaders to generate both LUTs.

For the Sky View texture, I ended up with the following code:

Excerpt of the Sky View LUT

1vec3 getSkyViewForward(vec3 up) {2// Project the sun direction onto the local horizon so azimuth has a stable reference.3vec3 projectedSun = sunDirection - up * dot(sunDirection, up);4return normalize(projectedSun);5}67vec3 getSkyViewRayDir(vec2 uv, vec3 up) {8vec3 forward = getSkyViewForward(up);9vec3 right = normalize(cross(forward, up));1011// Horizontal angle around the sky, centered around the projected sun direction.12float azimuth = (uv.x * 2.0 - 1.0) * PI;1314// Quadratic mapping: uv.y still covers [-PI/2, PI/2],15float elevation = (uv.y * uv.y - 0.5) * PI;1617float cosElevation = cos(elevation);18vec3 horizontal = cos(azimuth) * forward + sin(azimuth) * right;1920return normalize(horizontal * cosElevation + up * sin(elevation));21}2223void main() {24vec3 rayOrigin = uCameraPosition;25vec3 up = normalize(rayOrigin);26vec3 rayDir = getSkyViewRayDir(vUv, up);27vec3 planetCenter = vec3(0.0);2829vec2 atmosphereHit = raySphereIntersect(rayOrigin, rayDir, planetCenter, atmosphereRadius);30vec2 planetHit = raySphereIntersect(rayOrigin, rayDir, planetCenter, planetRadius);3132// Skip rays that never enter the atmosphere.33if (atmosphereHit.y <= 0.0) {34gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);35return;36}3738// March only through the visible atmospheric segment, stopping early if the ray hits the planet.39float atmosphereNear = max(atmosphereHit.x, 0.0);40float atmosphereFar = atmosphereHit.y;41if (planetHit.x > atmosphereNear) {42atmosphereFar = min(atmosphereFar, planetHit.x);43}4445float atmosphereSegmentLength = atmosphereFar - atmosphereNear;46float stepSize = atmosphereSegmentLength / float(SKY_VIEW_STEPS);4748// Same atmospheric scattering loop as before, but this time along the49// Sky View ray direction and using the Transmittance LUT for sunlight.5051// ...5253gl_FragColor = vec4(scatteredLight, 1.0);54}

The major thing to highlight here is the `getSkyViewRayDir`

, which defines our raymarching ray directions. In this case:

- The x-axis, vUv.x maps to the
**azimuth**, i.e., left-to-right directions from`[-PI, PI]`

. - Finally, we turn those two angles into a 3D
`rayDir`

:`up`

points toward the sky,`forward`

points along the horizon toward the sun, and`right`

lets us sweep left and right around the sky.

With this definition of our `rayDir`

, our raymarching loop here yields a texture representing the color of the sky for directions across the entire sky dome.

When it comes to the Aerial Perspective, as mentioned earlier, I slightly diverged from Hillaire’s paper. My resulting texture is a 2D texture where each pixel corresponds to one visible screen pixel. I rely on the depth buffer of the scene to tell how far along the ray we should march and accumulate scattering.

As a result, this lets me reuse more or less the same scattering code introduced in the first part, except that now each sample pulls sunlight visibility from the Transmittance LUT. The output stores the accumulated atmospheric scattering in RGB and a packed view transmittance value in alpha, which we will use later during composition.

Excerpt of the Aerial Perspective LUT

1void main() {2float depth = texture2D(depthBuffer, vUv).x;34// Reconstruct the world-space position for this screen pixel from the depth buffer.5vec3 rayOrigin = uCameraPosition;6vec3 worldPosition = getWorldPosition(vUv, depth);7vec3 rayDir = normalize(worldPosition - rayOrigin);8float sceneDepth = logDepthToRayDistance(vUv, depth);910vec2 atmosphereHit = raySphereIntersect(rayOrigin, rayDir, vec3(0.0), atmosphereRadius);11vec2 planetHit = raySphereIntersect(rayOrigin, rayDir, vec3(0.0), planetRadius);1213if (atmosphereHit.y <= 0.0) {14gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0);15return;16}1718// March only through the visible part of the atmosphere:19// stop at the scene depth, or earlier if the ray hits the planet.20float atmosphereNear = max(atmosphereHit.x, 0.0);21float atmosphereFar = atmosphereHit.y;2223if (planetHit.x > 0.0) {24atmosphereFar = min(atmosphereFar, planetHit.x);2526if (sceneDepth < planetHit.x - 2.0) {27atmosphereFar = min(atmosphereFar, sceneDepth);28}29} else {30atmosphereFar = min(atmosphereFar, sceneDepth);31}3233float segmentLength = atmosphereFar - atmosphereNear;34float stepSize = segmentLength / float(AERIAL_PERSPECTIVE_STEPS);3536// Same scattering loop as before, but along the view ray for this pixel.37for (int i = 0; i < AERIAL_PERSPECTIVE_STEPS; i++) {38float t = atmosphereNear + (float(i) + 0.5) * stepSize;39vec3 samplePoint = rayOrigin + rayDir * t;4041// Instead of raymarching toward the sun, look up sunlight visibility.42vec3 sunTransmittance = sampleTransmittanceLUT(samplePoint, sunDirection);4344// Accumulate Rayleigh and Mie scattering using sunTransmittance.45// ...46}4748// RGB stores scattered light; alpha stores view transmittance for composition.49gl_FragColor = vec4(scatteredLight, packedTransmittance);50}

With the Sky-view and Aerial Perspective LUTs generated, we have only one step remaining: combining them in a final post-processing pass to achieve the full LUT-based atmospheric scattering result. The code mainly consists of:

- Converting the current rayDir into skyViewUV coordinates, so given any direction in the sky, we know where to sample the precomputed Sky-view LUT.

1vec2 getSkyViewLUTUv(vec3 rayDir, vec3 planetCenter) {2vec3 up = normalize(uCameraPosition - planetCenter);3vec3 forward = getSkyViewForward(up);4vec3 right = normalize(cross(forward, up));56float vertical = clamp(dot(rayDir, up), -1.0, 1.0);7vec3 horizontal = rayDir - up * vertical;89// Convert the 3D ray direction back into the same azimuth/elevation10// coordinates used when generating the Sky View LUT.11float azimuth = atan(dot(horizontal, right), dot(horizontal, forward));12float elevation = asin(vertical);13float elevation01 = clamp(elevation / PI + 0.5, 0.0, 1.0);1415return vec2(16azimuth / (2.0 * PI) + 0.5,17sqrt(elevation01)18);19}2021vec3 sampleSkyViewLUT(vec3 rayDir, vec3 planetCenter) {22vec2 uv = getSkyViewLUTUv(rayDir, planetCenter);23return texture2D(skyViewLUT, uv).rgb;24}

- Reconstructing the view ray from the depth buffer and checking whether that ray hits the planet.
- Applying the Aerial Perspective LUT to scene geometry, using its alpha channel as view transmittance and its RGB channels as scattered light.
- Sampling the Sky View LUT for background pixels.

1void mainImage(const in vec4 inputColor, const in vec2 uv, out vec4 outputColor) {2float depth = readDepth(depthBuffer, uv);3vec3 rayOrigin = uCameraPosition;4vec3 rayDir = normalize(getWorldPosition(uv, depth) - rayOrigin);5vec3 planetCenter = vec3(0.0);6vec2 planetHit = raySphereIntersect(rayOrigin, rayDir, planetCenter, planetRadius);7vec3 color = inputColor.rgb;89bool isBackground = depth >= 1.0 - 1e-7;1011// For scene geometry, blend the original color with the atmospheric haze.12if (aerialPerspectiveEnabled && !isBackground) {13vec4 aerialPerspective = sampleAerialPerspectiveLUT(uv);14color = color * aerialPerspective.a + aerialPerspective.rgb;15}1617// For background pixels, replace the empty background with the sky color.18if (skyViewEnabled && isBackground) {19color = inputColor.rgb + sampleSkyViewLUT(rayDir, planetCenter);20}2122color = ACESFilm(color);23color = pow(color, vec3(1.0 / 2.2));2425outputColor = vec4(color, 1.0);26}

The playground below contains all the full implementation of our LUT-based atmosphere: all the LUTs and their corresponding shader, as well as the final post-processing pass. It is a bit dense, so I’d recommend checking the implementation directly at this Github link, where you’ll find the code that renders the scene below.

This version of atmospheric scattering may look almost identical to the one we worked on in the earlier parts of this post, but the underlying process is different: **we split the work into smaller LUTs that we then compose in the final effect**. Most importantly, instead of repeatedly raymarching toward the sun to figure out how much light reaches each sample, we can fetch that lighting information directly from the Transmittance LUT, replacing a costly nested loop with a simple texture lookup and resulting in a non-negligible performance boost for the final scene.

Despite that, my LUT-based implementation pales in comparison to what Sébastian Hillaire and others in the field came up with:

- There’s some banding and flickering happening, particularly in the sky-view
- The shortcuts I took made the process less optimal than it could have been.
- I should probably have used WebGPU from the get-go.

If you want to look at a real production-grade implementation, I highly recommend checking out three-geospatial by Shoda Matsuda (@shotamatsuda). His work on skies, clouds, and geospatial rendering has been a huge reference point for me, and the images he shares on social media speak for themselves.

Nonetheless, I learned *a lot* throughout this entire project, especially through the LUT-based approach, which took me out of my comfort zone when it comes to creating screen-space depth-aware post-processing effects. It also consolidated some previous learnings, and resulted in a series of beautiful visuals (which is the most important after all).

I’m very happy with the result of those experiments. I also worked on adding volumetric clouds on top of that, but the result is still a bit of a mixed bag and needs more work put into it before I could be proud enough of it to showcase it in a write-up. This will have to wait. Until then, I’m looking forward to leveraging that work to complement my upcoming projects and scenes *I have been slowly shaping in my head*.

Real-time Cloudscapes with Volumetric Raymarching introduces a lot of concepts used here.

This is a workaround to avoid too much blinking of the skyview at a large distance