---
title: The Beam Engine
source: https://glinscott.github.io/beam-engine/
author:
- '[[glinscott]]'
published: '2026-07-22'
created: '2026-07-24'
manifest_dates:
- '2026-07-24'
description: 'Article URL: https://glinscott.github.io/beam-engine/ Comments URL:
  https://news.ycombinator.com/item?id=49007221 Points: 378 # Comments: 74'
tags:
- clippings
extraction_status: success
pipeline_stage: ingested
id: 9ee70f16c6cfd0cd
---

This is a beam engine. It produced about fifteen horsepower continuously, roughly as much power as 150 people. Engines like this turned steam into the power that drove the Industrial Revolution. This article builds the engine up from first principles, using interactive figures to explore each idea (try rotating the engine above with two fingers, or pinching to zoom indragging the engine above, or zooming with ⌘/Ctrl + scroll). Let's start our journey through the engine with steam.

## Steam

Below, we have a pot filled with water and a fire underneath. As the fire heats the water, some of it begins to boil and turns into steam.

Steam undergoes an amazing transformation: it expands to **1,700 times** the volume of the original water. One cup of water becomes roughly 400 litres of steam, enough to fill two bathtubs. If the steam doesn't have enough room to expand it will push on all the walls of the container. This push on every wall is *pressure*, and we will measure it in atmospheres, multiples of the ordinary pressure of the air around us. The steam also presses on the surface of the water, which transmits the pressure evenly to everywhere the water touches.

Now we need a way to harness the properties of steam.

## Pistons and cylinders

A *piston* is a round disc that fits snugly inside a *cylinder*. Steam pushes on one face of the piston and a rod transmits the force elsewhere. The force depends on two things: the pressure of the steam and the area of the piston. At a pressure difference of one atmosphere, each square centimetre of piston provides about one kilogram of force.

Early boiler builders didn't know how to safely harness high-pressure steam.1 Instead, to get more force they made the piston wider. Because area grows with the square of the diameter, doubling the width of a piston gives it four times the area and four times the force at the same pressure. This is why early steam engines had enormous cylinders, sometimes wide enough for a person to stand inside. In the figure below, the boiler pressure never changes; try increasing only the bore until the piston can lift the car.

With steam pushing on our piston, we can do real work. But low-pressure steam is not very strong. To move heavy machinery, engineers turned to a surprising source: the atmosphere.

## The weight of air

Air feels weightless, but only because we are surrounded by it. Imagine a column of air one centimetre square, extending from your hand all the way to the top of the atmosphere. That column weighs about one kilogram, so the atmosphere presses on every square centimetre with roughly one kilogram of force.

We do not feel this enormous pressure because the air and fluid inside us push back at the same pressure. But if the pressure falls on one side of a surface, the pressure on the other side remains. This is what happens when you drink through a straw. Your mouth lowers the pressure inside the straw, and the atmosphere pushing on the drink in the cup forces it upward.

Otto von Guericke gave a spectacular demonstration of this effect in 1654. He joined two copper hemispheres into a sphere about half a metre across and pumped out the air. To the amazement of the observers, teams of horses could not pull the halves apart. The atmosphere was clamping them together with about two tonnes of force! As soon as he opened a valve and let the air back in, they came apart by hand.

Creating a vacuum was extremely difficult at first. Guericke had to laboriously pump the air out of his sphere, but steam gives us a much faster way to make one. If we fill a vessel with steam and then cool it with a spray of water, the steam condenses back into roughly 1/1,700 of its volume.

Fill a cylinder with steam, condense it underneath a piston, and the atmosphere will drive the piston down into the vacuum. A near-perfect vacuum gives us the same pressure difference we used earlier: about one kilogram of force for every square centimetre of piston. A piston half a metre across could collect almost two tonnes of force from the atmosphere.

## Newcomen's engine

In the early 1700s, mines were getting deeper, and flooding was becoming a huge problem. Once a shaft reached below the water table, water seeped in continuously and had to be pumped out day and night. The pumps were driven by teams of horses walking in circles. As one team tired, another took over, but the deepest mines still flooded during wet weather and valuable coal had to be abandoned. A new solution was needed, and steam would provide the answer.

Thomas Newcomen supplied tools to the mines and knew that flooding was both a huge problem and an opportunity. He spent years turning the vacuum piston stroke into an engine that could run all day. He connected the piston to one end of a huge rocking beam and hung heavy pump rods from the other. The atmosphere drove the piston down and lifted the pump rods; their weight then pulled the piston back up while the cylinder filled with steam again.

Newcomen's first successful engine was installed at a coal mine near Dudley in 1712. It ran at about twelve strokes per minute, lifting roughly forty-five litres of water fifty metres on every stroke. Unlike the horses, it could continue around the clock without food or rest. Similar engines soon appeared in mines from Cornwall to Newcastle.3

Newcomen's engine worked! But it used an extraordinary amount of coal. The cold water sprayed directly into the cylinder, chilling a huge mass of iron along with the steam. Roughly three quarters of the steam was wasted heating the cylinder back up on every stroke.

The mines were happy with this tradeoff because they burned *slack*, small pieces of coal that were considered waste. Anywhere else, the fuel cost was simply too much. This kept the steam engine stuck in coal mines for the next fifty years.

## The boiler

Why did Newcomen use the atmosphere to push the piston instead of the steam itself? His boiler was simply not strong enough. The *haystack boiler* produced only about a twentieth of an atmosphere above the surrounding air. It was built from thin copper or iron plates joined with rivets, and the wide walls and weak seams could not safely hold much pressure.

James Watt, who we will meet in the next section, used the *waggon boiler* shown below. Water sat in the broad chamber above the furnace, the hot gases passed underneath, and steam collected beneath the rounded roof.

The broad bottom was good at catching heat, but the waggon shape was terrible at holding pressure. Raise the steam pressure in the figure below and compare what happens to the rounded roof, the flat sides and the inward-curved bottom.

The figure also shows why later builders curved the whole boiler outward like the roof. They rolled iron plate into long cylinders, removing the flat sides and inward-curved bottom. They kept the boilers narrow because making a cylinder wider increases the force trying to split it open, even when the pressure stays the same.4 Better iron and riveting then made much higher pressures possible, and around 1800 Richard Trevithick was running engines at several atmospheres.

Now Newcomen's use of a vacuum makes sense. His boiler could push with perhaps fifty grams per square centimetre above atmospheric pressure. By condensing the steam and letting the atmosphere push the piston instead, he got close to one kilogram per square centimetre, around twenty times as much force from the same boiler.

## Watt's separate condenser

In 1765, Watt was repairing a model Newcomen engine at the University of Glasgow. He was amazed by how much steam it consumed and began trying to understand where it all went. He discussed the problem with his colleague Joseph Black, who was studying the heat absorbed while water boils. Black called it *latent heat*. For a kilogram of water, boiling it away takes more than five times as much energy as heating it from freezing to boiling.

With this knowledge, Watt calculated the exact amount of water needed to condense the volume of steam in the cylinder. He was surprised to find that this exact amount barely made a vacuum at all: the condensing steam dumped its latent heat into the spray, warming the water until it stopped condensing anything. Adding in more cold water just cooled the cylinder down more, wasting steam to heat the cylinder back up on the next stroke. Watt's brilliant insight was to add a second vessel that could stay cold while the cylinder stayed hot.5

At the end of the stroke, a valve opened and the steam rushed into the cold vessel, called the *condenser*. As the steam turned back into water, the pressure fell in the condenser and, through the connecting pipe, in the cylinder as well. A small *air pump* driven by the engine drew out the condensed water, along with any air that had leaked in, on every stroke. Keeping the cylinder hot and the condenser cold cut coal consumption by about two thirds! Watt and his business partner Matthew Boulton turned the saving into a business model, charging customers one third of the money they saved on coal.

Better tools for making precise cylinders allowed Watt to make another important change: he closed the top of the cylinder and used steam on both sides of the piston. Steam pushed down while the condenser lowered the pressure below; on the return stroke, the same thing happened in the opposite direction. This was the *double-acting* engine. Below, we can compare it with the single-acting cylinder it replaced.

The same cylinder now produced power on both strokes, and the steady push-pull made the engine much better suited to driving machinery. But getting steam in and out of the cylinder was now more complicated. One end had to connect to the boiler while the other connected to the exhaust, and then the two connections had to switch before the piston returned.

## The slide valve

Early steam engines used several separate valves and linkages to route the steam. Our engine does all of this with one *slide valve*. It moves only a few centimetres, connecting one end of the cylinder to fresh steam and the other to the exhaust. As the piston reaches the end of its stroke, the valve slides across and swaps the two connections.

The valve sits inside the *steam chest*, an iron box bolted to the side of the cylinder and kept full of fresh steam. Three ports open into the chest. The two outer ports connect to the ends of the cylinder, while the middle one carries away the exhaust. The valve is shaped like a wide, hollow D. One edge uncovers a cylinder port and lets fresh steam enter, while the hollow back joins the other cylinder port to the exhaust.

The valve needs to move in perfect synchronization with the piston, or the engine will not work. This motion comes from an *eccentric* on the engine's rotating shaft. The eccentric is a circular disc mounted slightly off-centre, so its centre travels in a small circle as the shaft turns. A strap around the disc follows this motion and drives the valve rod back and forth. Its position on the shaft is chosen so the next steam port begins opening before the piston reaches the end of its stroke.

Now, we can see how the piston, valve gear and eccentric work on our beam engine.

### Using less steam

We can save a surprising amount of coal by closing the steam port before the piston reaches the end of its stroke. The trapped steam continues to expand and push the piston, although its pressure falls as the volume grows. Closing the valve at halfway, called *cutoff*, uses half as much steam while still producing about 85 percent of the ideal work.6 Watt patented this idea in 1782. Later compound engines sent the exhaust from one cylinder into a larger cylinder, then sometimes into a third, extracting more work as the steam expanded.

### Measuring the work

Everything we have just discussed happens inside an opaque cylinder. In 1796, Watt's assistant John Southern built an instrument that let them see inside. A small spring-loaded piston moved a pencil up and down with the pressure, while a card moved sideways with the main piston. The resulting *indicator diagram* showed the pressure through the entire stroke, and the area inside the loop measured the work produced.

A leaking piston, late cutoff and restricted exhaust each produce a different shape, allowing an engineer to diagnose the engine from a single card. Boulton & Watt found the instrument so valuable that they kept it secret for years.7

We can now control the steam and produce power in both directions, but the piston still moves back and forth. This is called *reciprocating motion*. Pumps can use it directly, but the mills driving the Industrial Revolution needed rotation.

## Making rotation

To turn the piston's back-and-forth motion into rotation, our beam engine uses a *crank*, although Watt's first rotating engines could not use one.8 A pin offset from the centre of the shaft is joined to the piston by a *connecting rod*. The push on the pin turns the shaft, but not equally through the revolution. Twice per turn the crank and connecting rod line up, at positions called *dead centres*, where the piston pushes straight through the shaft and produces no rotation at all. With nothing to carry it past these points, the engine would stop the first time the crank reached one.

The large *flywheel* fixes this problem. It stores energy while the crank has good leverage, then returns that energy to keep the engine spinning past the dead centres. In the figure below, the shaded band in the inset shows the flywheel collecting and repaying energy through each revolution. Try the flywheel mass slider: a heavier wheel changes speed less, giving the engine a smooth and steady rotation.

Our engine can now turn a shaft without stopping. But joining the piston rod to the crank turns out to be harder than it looks.

## The beam and the parallel motion

Now, look closely at the connecting rod in the figure below. As the crank turns, its pin moves sideways as well as up and down. The piston rod cannot follow it because it must travel straight through the seal at the top of the cylinder. If we connect them directly, the rod pushes the piston sideways and quickly destroys the seal.

The beam carried the sideways load into a large round bearing, which workshops could make accurately. But its end moved in an arc, and Watt still needed the piston rod to travel in a straight line.

His ingenious solution was the *parallel motion*, patented in 1784. A set of hinged links joins the beam to a fixed point on the engine. As the beam pulls the piston rod sideways in one direction, another link pulls it almost exactly the same amount in the other. The two curves cancel, leaving a path that is remarkably close to a straight line. Watt was so pleased with the mechanism that he wrote he was “more proud of the parallel motion than of any other mechanical invention I have ever made.”

Our piston can now turn the crank without being pulled sideways. At the far end of the beam, we also get a convenient source of back-and-forth motion, which the engine uses to keep its boiler filled with water.

## The pump

As the engine runs, the boiler turns water into steam. To keep it going, we need to replace that water without stopping. We can't simply connect a water tank, because the pressure inside the boiler would push the water back out. Instead, the far end of the beam drives the small pump beside the base of the engine, forcing fresh water into the boiler.

Inside the pump is a narrow plunger and two one-way *check valves*. As the plunger rises, the pressure falls, the inlet valve opens and water enters from the tank. On the way down, the pressure rises, closing the inlet valve and opening the outlet towards the boiler. The changing water pressure operates both valves automatically.

The pump must produce slightly more pressure than the boiler, but it does not need to move much water on each stroke. Making the plunger narrow keeps the required force small, for the same pressure-times-area reason that made our engine piston wide. A small part of the engine's power can now keep the boiler full, while the rest turns the flywheel.

## Powering the mill

We talked about why mills need rotation, but not how they used it. Before steam engines, water-powered mills had to sit beside a river. The flowing water turned a large waterwheel, which drove a main shaft, and iron shafts, pulleys and leather belts carried that rotation through the building to power the machines. Our example mill here has a saw for cutting wood and a power loom which wove cloth. Click either machine to shift its belt onto the loose pulley; that machine will coast to a stop while the shaft and the other machine continue running.

It is not intuitive that a leather belt can transmit enough power to drive a machine that ten strong people could not. With only friction between the iron pulleys and the leather providing the connection, it seems that the belt would slip. The physics underlying friction is fascinating. Imagine a huge ship tied to an iron bollard on the dock with a rope. Tension in the first small part of the rope presses it against the iron, and the resulting friction reduces the tension that reaches the next part, and so on around the post.9

Now, let's return to leather belts and iron pulleys. A belt is installed under tension, so at rest its two sides pull with roughly equal force. Once the machine needs power, friction transfers some of that pull from the returning side to the driving side.10

The power transferred by a belt is the difference in tension multiplied by the belt speed. At full mill scale, a sixteen-foot flywheel at sixty revolutions per minute has a belt speed of about fifteen metres a second. If the load makes one side pull with 2,000 newtons more than the other, a foot-wide leather belt can carry about forty horsepower.

### The fight for water

Richard Arkwright's water-powered mill at Cromford opened in 1771, and the factory system that followed created fierce demand for the best river sites. Water-powered mills were also dependent on the weather: a dry season could shut down the factory.

Steam pumping engines offered a solution. An engine lifted the water that had passed beneath the wheel back up the hill, allowing the same water to fall through the wheel again. This kept the smooth turn of the water wheel, but wasted coal moving the water. Watt sold sixteen to twenty horsepower pumping engines to deliver ten horsepower to the machines.

Watt's double-acting engine, beam, crank and flywheel let the engine directly turn the line shaft. This met a huge demand from mill owners who wanted to build near workers and materials rather than around a particular stretch of river.11 One problem remained, though: every time a machine was turned on or off, the load on the engine changed.

## The governor

The beam engine still needed a way to keep its speed constant. Imagine it at the beginning of the day, turning at 30 rpm with no machines connected. When the first machine is connected, it draws power from the engine and slows it down. The engine driver could open the throttle by hand until the shaft returned to 30 rpm, but this was tiring work, and mistakes had severe consequences. A cast-iron flywheel could burst if it spun too quickly.

Instead, Watt adapted a device used on windmills to adjust the steam automatically.12 Bevel gears turn a vertical spindle, and two heavy balls hang from hinged arms attached to it. As the engine speeds up, the balls swing outward and lift a sliding collar. A fork and long rod carry this motion across the engine and turn the *steam cock* towards closed. When the engine slows, the balls fall and open the cock again.13

## The whole machine

Let's return to the complete engine from the beginning of the article. Every mechanism we studied on its own is here, running in its place. The figure follows the power once along its whole path, from the boiler steam to the belt that leaves for the mill.14

## Epilogue

The beam engine was a product of the tools and science of its time. Watt used a beam and parallel motion partly because the workshops of the 1780s could not make long, accurate guides for a crosshead. As planing machines improved during the nineteenth century, those straight guides became practical. The heavy beam was no longer required, and by the 1860s most new mill engines drove the flywheel directly.15

Line shafts and leather belts outlived the beam engine, remaining above factory floors well into the twentieth century. Electric motors finally gave each machine its own source of rotation. Wires replaced the long shafts and belts, and stopping one lathe no longer changed the load on a central engine driving the entire mill.

The most dramatic change was how much power newer engines extracted from coal. Corliss valves controlled steam expansion more precisely, compound engines expanded it through several cylinders, and turbines eventually replaced the piston with a continuously rotating wheel. Newcomen converted only about half a percent of the heat into useful work. Watt's condenser raised the useful share to roughly three percent, enough for steam power to move away from the coal mines. By the 1890s, high pressure and compound expansion pushed large marine engines such as the Titanic's beyond ten percent. A modern steam turbine plant converts more than forty percent.

## Footnotes

Thomas Savery tried to use higher-pressure steam in the 1690s with boilers made from soldered copper. The fire could soften the solder, and the leaking joints needed frequent repair. Newcomen took a different route. Because the steam in his boiler was barely above atmospheric pressure, he could use thin lead and wrought-iron plates joined with rivets. The seams still leaked and the metal corroded, but the boiler did not have to contain the pressure that Savery's pump required. ↩

Casting a large iron cylinder was much easier than making the inside straight and round. Newcomen's cylinders were ground by hand, then sealed with a leather flap covered by a layer of water, which could follow the uneven bore. Denis Papin had proposed the vacuum-piston principle in 1690: a small amount of water boiled beneath a piston and pushed it upward, then condensation allowed the atmosphere to force it down again. His apparatus demonstrated a single stroke but did not become a continuously running engine. ↩

A piston 50 centimetres across has about 2,000 square centimetres of area, enough to collect two tonnes of force from a perfect vacuum. After allowing for leaks and the weight of the pump rods, it might do about four kilowatts of useful work. A horse can sustain much less than one horsepower over a working day, so replacing the engine required a relay of perhaps fifteen or twenty animals. Watt later sold his engines by the number of horses they replaced, and fixed one horsepower at 33,000 foot-pounds per minute. ↩

For a barrel with radius

*r*and length*L*, the cut has an area of 2*rL*, so pressure*p*pushes the halves apart with a force of 2*prL*. Two edges of length*L*resist that force, leaving*pr*in each metre of plate. At two atmospheres and a half-metre radius, this is about ten tonnes per metre. The stress running lengthwise is only half as large, which is why a cylindrical boiler tends to split along its length like a sausage. A sphere divides the load equally and is stronger still, but it was much harder to make from rolled and riveted plate. ↩Watt's engine needed a much more accurate cylinder than Newcomen's loose, water-sealed piston. Around 1775, the ironmaster John Wilkinson built a boring mill with a rigid cutting bar supported at both ends, adapting techniques he had developed for boring cannons. In 1776, Matthew Boulton reported that a 50-inch cylinder installed at Tipton varied by less than the thickness of an old shilling. This accuracy kept the steam from leaking around Watt's piston and made the new engine practical. ↩

For a cylinder with volume

*V*and pressure*p*, admitting steam for the full stroke produces work*pV*. With cutoff at half stroke, the admitted steam produces*pV*/2 during the first half. As it expands through the rest of the cylinder, it adds about 0.35*pV*more, assuming it follows Boyle's law and remains hot. This gives 85 percent of the full-stroke work from half the steam. Cutting off earlier saves still more steam, but eventually the falling pressure becomes too weak to overcome friction and the poor leverage near dead centre. ↩The pressure and volume graph outlived the mechanical indicator. In 1834, Émile Clapeyron used the same type of diagram to explain Sadi Carnot's theory of heat engines, and thermodynamics still plots pressure against volume today. ↩

-
James Pickard patented the use of a crank on a steam engine in 1780, so William Murdoch designed the

*sun-and-planet gear*as a way around the patent. A gear attached to the connecting rod travelled around a second gear on the flywheel shaft, turning the shaft twice for every cycle of the beam. Once Pickard's patent expired in 1794, builders returned to the much simpler crank used on our engine.Murdoch's mechanism belongs to the

*epicyclic*, or planetary, family of gears. Several planet gears can share the load while the input and output remain on the same axis, making the arrangement compact and strong. Planetary gears appear in cordless drills, bicycle hubs, automatic transmissions and wind turbines. Hybrid cars even use them to divide power between the engine, electric motor and wheels. ↩ -
If we slice the wrapped rope into small pieces and add the force vectors, each piece has a small inward force equal to the local tension multiplied by the angle it covers. Friction can remove up to

*μ*times that inward force, about 0.3 for rope on cast iron.Repeating that fractional reduction produces the exponential

*e*−μθ. With a 2,000-newton pull, about the weight of an upright piano, one turn around the post leaves 300 newtons, two leave 46, and three leave seven. ↩ A flat belt tends to wander off a truly cylindrical pulley. Millwrights made the pulley slightly larger at the centre, forming a shallow

*crown*that continually steers the belt back. When the belt arrives off-centre it first meets a coned surface, and the tilted contact carries its leading edge a little towards the crown on each turn. Once centred, both halves of the crown steer equally and the belt remains centred. This simple change kept the belt on the pulley without guides. ↩Between 1775 and 1800, the Boulton & Watt partnership built 496 engines. Thirty-eight percent were pumping engines, while sixty-two percent produced rotation, mostly for the textile industry. ↩

In 1788, Boulton told Watt that he had seen spinning balls used to regulate millstones in Manchester. Watt adapted the mechanism to steam engines, but never patented the borrowed idea. ↩

The height of the balls gives a surprisingly direct measurement of speed. Balancing their outward motion against gravity gives

*h*=*g*/*ω*2, where*h*is the vertical distance below the hinge. The mass cancels, so heavier balls push harder on the linkage but rise to the same height. At the crankshaft's speed the arms would need to be about a metre long, so the bevel gears spin the governor faster and let it fit on the short pillar. ↩The oldest rotative engine still in existence, installed at Whitbread's brewery in London in 1785, is built to the same pattern as ours. Its cylinder was 64 centimetres across and the piston swept 1.8 metres on each stroke, a column of steam taller than a person. The flywheel, 4.3 metres across, turned twenty times a minute — a leisurely one revolution every three seconds — burning roughly forty kilograms of coal an hour. Watt rated it at ten horsepower, and it replaced the wheel of horses that had driven the brewery's mills. When it was converted to double action in 1795, the same cylinder was re-rated to fifteen horsepower; the brewery declined twenty, because Boulton & Watt's annual fee rose with the power. It stayed at work for a hundred and two years. ↩

American paddle steamers kept the beam engine into the 1880s, mounting a

*walking beam*high above the deck. Their paddle wheels needed high torque at only about twenty revolutions per minute, and a shallow riverboat had more room above the water than below it. Ocean-going ships folded similar machinery into the hull, then moved to smaller and faster engines as the screw propeller replaced the paddle wheel. ↩