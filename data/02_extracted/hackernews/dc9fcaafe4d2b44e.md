---
title: Xorg-server 26.1.0 rc1
source: https://lists.x.org/archives/xorg-announce/2026-August/003741.html
author:
- '[[st_goliath]]'
published: '2026-08-20'
created: '2026-08-20'
manifest_dates:
- '2026-08-20'
description: ''
tags:
- clippings
extraction_status: success
pipeline_stage: fact_extracted
id: dc9fcaafe4d2b44e
source_type: community_discussion
tldr: X.Org 发布 xorg-server 26.1.0 首个候选版本 26.0.99.901，打包了 Xorg、Xephyr、Xnest、Xvfb、Xwin、Xquartz
  等全部非 Xwayland 服务器。主要变化包括构建系统迁移到 meson、默认禁用字节交换客户端与字体服务器连接，以及 Xvfb 新增多 CRTC 支持。
objective_summary: Alan Coopersmith 于 2026 年 8 月 20 日在 xorg-announce 邮件列表宣布 xorg-server
  26.0.99.901（即 26.1.0 rc1）发布，该候选版本收录了自 21.1 分支以来的全部改动并附带 SHA256/SHA512 校验值与 PGP 签名。新版移除了
  autoconf/automake 构建系统仅保留 meson，默认禁止字节交换客户端与字体服务器连接，并新增 DPMS 1.2 的 DPMSInfoNotify
  事件及 XFixes 6.1 支持。Xorg 新增 BSD 平台的 DRM 支持并将非 root 用户日志移至 $XDG_STATE_HOME/xorg，Xvfb
  支持多 CRTC 与最多 13 个鼠标按键。维护者建议测试者搭配 2026 年 3 月发布的 libpciaccess 0.19 构建运行。
event_type: infrastructure_update
epistemic_status: verified_fact
entities:
  companies:
  - X.Org Foundation
  - Oracle
  - freedesktop.org
  technologies:
  - Xorg
  - Xephyr
  - Xnest
  - Xvfb
  - Xwin
  - Xquartz
  - Xwayland
  - meson
  - DRM
  - DPMS
  - XFixes
  - libpciaccess
  - glamor
  - EGL
  key_people:
  - Alan Coopersmith
  - Adam Jackson
  - Aaron Plattner
  - Aaron Dill
  - Aki Sakurai
key_logic_flow:
- Alan Coopersmith 于 2026 年 8 月 20 日通过 xorg-announce 邮件列表宣布 xorg-server 26.0.99.901
  发布，这是 26.1.0 的第一个候选版本。
- 该候选版本打包了全部非 Xwayland 服务器，包括 Xorg、Xephyr、Xnest、Xvfb、Xwin（Windows 版）和 Xquartz（macOS
  版）。
- 构建系统方面移除了 autoconf/automake 仅保留 meson，并新增对 DPMS 1.2 的 DPMSInfoNotify 事件、XFixes 6.1
  以及 xorg.conf 中 AllowForceTerminate 选项的支持。
- 安全与默认行为方面，新版本默认禁止字节交换客户端连接，并默认禁用字体服务器连接。
- Xorg 新增 BSD 平台的 DRM 支持并将非 root 用户日志文件迁移到 $XDG_STATE_HOME/xorg，Xvfb 新增多 CRTC 支持并可识别最多
  13 个鼠标按键。
- 维护者建议测试者构建运行 Xorg 时搭配 libpciaccess 0.19，因为至少一个 bug 修复依赖该版本引入的新 API。
object_mentions:
- object_type: project
  name: xorg-server
  canonical_name: xorg-server
  url: https://xorg.freedesktop.org/archive/individual/xserver/xorg-server-26.0.99.901.tar.xz
  confidence: high
  article_role: primary_subject
  evidence_snippets:
  - xorg-announce 邮件列表发布公告，宣布 xorg-server 26.0.99.901 作为 26.1.0 的首个候选版本正式推出。
  - 该候选版本打包了全部非 Xwayland 服务器，包括 Xorg、Xephyr、Xnest、Xvfb、Xwin 与 Xquartz。
  - 公告详细列出了自 xorg-server 21.1 以来的主要变更，包括移除 autoconf 构建系统、默认禁用字节交换客户端和字体服务器连接等。
  article_id: dc9fcaafe4d2b44e
- object_type: project
  name: libpciaccess
  canonical_name: libpciaccess
  url: null
  confidence: medium
  article_role: ecosystem_context
  evidence_snippets:
  - 公告建议 Xorg 测试者使用 2026 年 3 月发布的 libpciaccess 0.19 进行构建和运行。
  - 至少一个 bug 修复依赖 libpciaccess 0.19 引入的新 API，该 API 仅在 meson 构建检测到新版本时才会被调用。
  article_id: dc9fcaafe4d2b44e
extract_result: success
---

# [ANNOUNCE] xorg-server 26.0.99.901

**Alan Coopersmith**
alan.coopersmith at oracle.com

*Thu Aug 20 02:01:40 UTC 2026*

As per the schedule, I am pleased to announce xorg-server 26.0.99.901,
the first release candidate of the upcoming xorg-server 26.1.0 release
(or xorg-server 26.1.0 rc1 for short).
This contains all of the remaining non-Xwayland servers, including Xorg,
Xephyr, Xnest, Xvfb, Xwin (for Microsoft Windows) and Xquartz (for MacOS).
Some notable changes since xorg-server 21.1 include:
* Removal of autoconf/automake build system, leaving only meson
* Add support for DPMSInfoNotify event from DPMS 1.2
* Add support for XFixes 6.1 & AllowForceTerminate option in xorg.conf
* Disallow byte-swapped clients by default
* Disable font server connections by default
* Xorg: Add DRM platform for BSD
* Xorg: Move default non-root-user log files to $XDG_STATE_HOME/xorg
* Xvfb: Add multiple CRTC support
* Xvfb: Support up to 13 mouse buttons
* more tests included
Testing of this release candidate would be greatly appreciated.
Please report any issues at:
https://gitlab.freedesktop.org/xorg/xserver/-/issues
For those testing the Xorg server, we recommend building and running
against libpciaccess 0.19 (released in March 2026), as at least one of
the bug fixes depends on new API introduced in that release, which will
only be called if the new API is detected by meson at build time.
The following shortlogs include all the changes since the previous
xorg-server-21.1 branch was first created, though some are only relevant
to the separately released Xwayland or were already backported to the 21.1
branch (such as all of the CVE fixes).
git tag: xorg-server-26.0.99.901
https://xorg.freedesktop.org/archive/individual/xserver/xorg-server-26.0.99.901.tar.xz
SHA256: 24f16885a6152d9abb384a90c52b2e417fafdc474ff914d8faddf6b6b9566c45 xorg-server-26.0.99.901.tar.xz
SHA512: 67267e8af43cd8be0ee0bac984837114598a69817bda0219e703f0395c8624a81203a98f36240bfc74ce8524335ee0954104e99ece6b9ab3c1104adbf57c2c43 xorg-server-26.0.99.901.tar.xz
PGP: https://xorg.freedesktop.org/archive/individual/xserver/xorg-server-26.0.99.901.tar.xz.sig
Aaron Dill (1):
logind: call SetType on the logind session
Aaron Plattner (4):
modesetting: Only use GAMMA_LUT if its size is 1024
xfree86: NUL-terminate strings in hwEnableIO
os: print <signal handler called> if unw_is_signal_frame()
os: print registers in the libunwind version of xorg_backtrace()
Adam Jackson (17):
selinux: Stop using security_context_t
xinput: Silence a warning from gcc 11
xkb: Silence a warning from gcc 11
dmx: Fix some redeclaration warnings from gcc 11
ephyr/glamor: Port to EGL
glamor: Don't open-code epoxy_glsl_version()
ephyr: Don't open-code glamor_compile_glsl_prog
wayland/streams: Don't open-code glamor_compile_glsl_prog
glamor: Require EGL_KHR_no_config_context
glamor: Assume EGL in glamor_context
xwayland/glx: Enable sRGB fbconfigs
glx/dri: Filter out fbconfigs that don't have a supported pixmap format
ephyr: Sync less in hostx_paint_rect
ephyr: Sync even less in ephyrInternalDamageRedisplay
present: Send a PresentConfigureNotify event for destroyed windows
glamor: Lift the GLX EGL backend from Xwayland
glamor/glxprov: Stop exposing non-db(-capable) configs
Aki Sakurai (2):
xquartz: fix compilation
xquartz: fix inverted tablet pen Y tilt on macOS
Alan Coopersmith (216):
Replace "the the" with a single "the" in docs & comments
xfree86: finish removing numTimings in xf86ValidateModes()
gitlab CI: enable gitlab's builtin static analysis
gitlab CI: enable commit & merge request checks
os: Use memcpy() instead of memmove() when buffers are known not to overlap
dix: Use memcpy() instead of memmove() when buffers are known not to overlap
mi: Use memcpy() instead of memmove() when buffers are known not to overlap
xf86AutoConfig: try modesetting on all platforms we build it on
Remove "All rights reserved" from Oracle copyright notices
gitlab CI: add workflow rules
Add a .mailmap file to canonicalize author names and emails
Revert "Compile lnx_platform.c on FreeBSD too."
os: Assume all supported non-WIN32 platforms have seteuid & saved_ids
unifdef apollo
unifdef SUNSYSV
bsd_init.c: fix build on FreeBSD
Xext: SProcSyncCreateFence needs to swap drawable id too
Xserver.man: Note that -byteswappedclients is the default in this release
xorg.conf.man: Add missing new paragraph mark before AllowByteSwappedClients
Xi: ProcXIGetSelectedEvents needs to use unswapped length to send reply
Xi: ProcXIPassiveGrabDevice needs to use unswapped length to send reply
Xquartz: ProcAppleDRICreatePixmap needs to use unswapped length to send reply
xf86_OSlib.h: Don't need to include Solaris keyboard headers here
solaris: convert APM interfaces to official SRN interfaces
CI: Checkout driver tag into the directory we build from
Move sizeof to second argument in calloc calls
meson: make AF_INET6 check work with stricter compiler flags
compiler.h: drop translation of Sun compiler platform defines to gcc
Remove remnants of support for SysV versions before SVR4
Remove remnants of support for SVR4 systems other than Solaris & illumos
dix: check for calloc() failure in Xi event conversion routines
dix: PolyText: fully initialize local_closure
dix: SetFontPath: don't set errorValue on Success
dix: enterleave.c: fix implicit fallthrough warnings
dix: CreateScratchGC: avoid dereference of pointer we just set to NULL
dix: InitPredictableAccelerationScheme: avoid memory leak on failure
dix: dixChangeWindowProperty: don't call memcpy if malloc failed
dix: ProcListProperties: skip unneeded work if numProps is 0
dix: HashResourceID: use unsigned integers for bit shifting
dix: GetPairedDevice: check if GetMaster returned NULL
dix: FindBestPixel: fix implicit fallthrough warning
CI: Update xcb util libraries to versions with working submodule URLs
CI: clone libdecor from fd.o instead of gnome.org
CI: update libdecor from 0.1.0 to 0.1.1
CI: update meson from 0.56.2 (bullseye) to 1.0.0 (bullseye-backports)
meson: list required version of xproto headers in xorg-server.pc
os: NextDPMSTimeout: mark intentional fallthroughs in switch
dix: Use __builtin_popcountl if available to replace Ones()
xfree86: avoid memory leak on realloc failure
Xi: avoid NULL pointer dereference if GetXTestDevice returns NULL
render: avoid NULL pointer dereference if PictureFindVisual returns NULL
dix: fix button offset when generating DeviceButtonStateNotify events
dix: limit checks to MAX_VALUATORS when generating Xi events
modesetting: avoid memory leak when ms_present_check_unflip() returns FALSE
dix-config.h: add HAVE_SOCKLEN_T definition
os: if getaddrinfo() is available, use it, even if IPv6 support is disabled
os: if inet_ntop() is available, use it for IPv4 addresses as well
ci: update XTS to a commit that doesn't require -fcommon workaround
xkb: ensure XkbAllocNames sets num_rg to 0 on allocation failure
xkb: Convert more sprintf calls to snprintf in xkbtext.c
xkb: Add tbGetBufferString helper function
pkgconfig files: Add URL
dix-config.h: define HAVE_STRUCT_SOCKADDR_STORAGE for xtrans 1.6
Xserver.man: remove X FireWall Proxy (xfwp) info
man pages: use .BR to mark up man page references
Xserver.man: allow line breaks in default font path
Xserver.man: add Xwayland(1) to list of server-specific man pages
Xserver.man: correct list of available authorization protocols
xfree86: make modeline2c.awk put a newline at the end of xf86DefModeSet.c
test: remove stray semi-colons after functions
modesetting: fix typo in XF86ModuleVersionInfo initialization
test: remove extra return
os: remove unused definition of BUGADDRESS
render: miindex.c does not need header guard macros
mi: use common implementation of bit counting function
man pages: strip trailing whitespace
man pages: remove extraneous PP macros
XWin.man: fix typos in font change escapes
man pages: don't use .BI macro with a single argument
Xephyr.man: Use \- to get ASCII hyphens instead of Unicode dashes
Re-export Ones()
xf86bigfont: fix -Wimplicit-function-declaration error
ci: enable xf86bigfont in one set of builds
xf86bigfont: fix -Werror=unused-variable build failure
xfree86: Fix builds with gcc -Wpedantic
ci: run builds with most options enabled and most options disabled
Xace: provide definitions of new hook functions when xace is disabled
dix: Fix builds with meson -Dxace=false -Dwerror=true
meson: don't build xselinux if xace is disabled
modesetting: Fix builds with pciaccess or udev_kms disabled
xwayland: fix builds with xace disabled
modesetting: fix modesetting symbol test when glx is disabled
meson.build: include Xephyr in output of which ddx we're building
panoramix: avoid null dereference in PanoramiXMaybeAddDepth()
panoramix: avoid null dereference in PanoramiXConsolidate()
test: add unit tests for x_sha1_* functions in os/xsha1.c
os: Use EVP APIs when building with OpenSSL 3
xfree86: fix meson build on 64-bit Solaris/SPARC systems
xfree86: add missing headers to build sun_init.c on Solaris/SPARC
meson: fix build if shmfence is enabled but dri3 & xwayland are not
xfree86: Fix -Wdiscarded-qualifiers warnings in SPARC Sbus probe code
Strip trailing whitespace from source files
Xext/shm: avoid null dereference in ShmInitScreenPriv()
Xext/sync: avoid null dereference if SysCounterGetPrivate() returns NULL
Xext/sync: avoid null dereference in init_system_idle_counter()
Xext/sync: Avoid dereference of invalid pointer if malloc() failed
Xext/vidmode: avoid null dereference if VidModeCreateMode() allocation fails
Xext/xres: avoid null dereference in ProcXResQueryClients()
Xext/xselinux: add fast path to ProcSELinuxListSelections()
Xext/xselinux: avoid memory leak in SELinuxAtomToSID()
Xext/xtest: avoid null dereference in ProcXTestFakeInput()
Xi: avoid null dereference if wOtherInputMasks() returns NULL
Xi: set value for led_values in CopySwapKbdFeedback()
Xi: handle allocation failure in ProcXGetDeviceDontPropagateList()
Xi: handle allocation failure in ProcXListInputDevices()
Xi: handle allocation failure in add_master_func()
dix: handle allocation failure in DeviceFocusEvent()
dix: avoid null dereference if wOtherInputMasks() returns NULL
dix: assert that size of buffers to swap is a multiple of the swap size
dix: handle allocation failure in ChangeWindowDeviceCursor()
dix: avoid memory leak in ProcListProperties()
dri: prevent out-of-bounds read in dri3_fd_from_pixmap
glamor: handle potential NULL return from GetPictureScreenIfSet()
glamor: handle allocation failure in glamor_create_pixmap()
glamor: silence false positive in glamor_validate_gc()
glamor: handle allocation failures in glamor_largepixmap.c
glamor: avoid null dereference in glamor_dash_setup()
glamor: avoid null dereference in glamor_composite_clipped_region()
glamor: avoid double free in glamor_make_pixmap_exportable()
Create a SECURITY.md file
dix: set errorValue correctly when XID lookup fails in ChangeGCXIDs()
os: make FormatInt64() handle LONG_MIN correctly
xfree86: remove leftover ev56.c source files
gitlab CI: add main branch to exception list for check-commits
xfree86: issue error if too many clocks entries are listed in config
os: add a generic -verbose option instead of making each server add its own
os: fix sha1 build error with Nettle 4.0
ephyr: add -title to Xephyr man page
ephyr: add -name to Xephyr man page
ephyr: show that -name & -title take non-optional arguments in usage output
CI: update URLs for freetype and font/util in cross-prereqs-build.sh
CI: update to libX11 1.8.2 & drop -fcommon workaround in cross-prereqs-build
os: use winsock2.h definitions on mingw in xserver_poll.h
os: include <assert.h> in ospoll.c
CI: Update debian image from bullseye (11) to bookworm (12)
meson: add install_tags to files meson couldnt guess on its own
meson: replace join_paths() with / operator
xf86: fix hotplug header include in platform_noop.c
CI: Catch UnicodeDecodeError in whitespace-check.py
glx: avoid null dereference in validGlxFBConfigForWindow()
Xvfb: handle allocation failure in vfbInstallColormap()
fb: quiet -Wanalyzer-out-of-bounds warnings in fbOverlayCopyWindow()
os: handle memory allocation failure in set_font_authorizations()
os: handle memory allocation failure in get_mcast_options()
present: prevent memory leaks in present_create_notifies()
randr: handle -Wanalyzer-null-dereference in ProcRRGetOutputInfo()
randr: handle -Wanalyzer-null-dereference in ProcRRListProviderProperties()
randr: handle -Wanalyzer-null-dereference in ProcRRGetScreenInfo()
render: handle -Wanalyzer-null-dereference in AllocateGlyphHash()
tests: plug leak of results in compute_expected_damage()
tests: Handle -Wanalyzer-possible-null-dereference in damage/primitives.c
xf86: drop no longer needed entries from default driver list for Intel
xkb: handle -Wanalyzer-null-dereference in XkbDDXLoadKeymapByNames()
xkb: plug memory leaks in InitKeyboardDeviceStructInternal() error paths
meson: define BSD44SOCKETS and LOCALCONN for xtrans when appropriate
meson: raise minimum supported version to meson 1.0.0
dix: Fix Collabora's name in copyright notices
COPYING: drop copyright & license notice for removed SCO code
COPYING: drop copyright & license notice for removed USL code
COPYING: drop copyright for removed non-evdev input drivers
COPYING: drop copyright for removed xf8_16bpp overlay module
COPYING: drop copyright & license notice for removed dlloader code
COPYING: drop copyright & license notice for removed glxvisuals.c
COPYING: drop copyright & license notice for removed DMX code
COPYING: drop copyright & license notice for removed xorgcfg code
COPYING: drop copyright & license notice for removed assyntax.h
COPYING: drop copyright & license notice for removed mibstore.h
COPYING: drop copyright & license notice for removed kdrive linux backend
COPYING: drop copyright & license notice for removed SysV os-support code
COPYING: drop copyright & license notice for removed extmod code
COPYING: drop copyright & license notice for removed lnx_font.c
COPYING: drop copyright & license notice for removed dmx input drivers
COPYING: drop copyright & license notice for removed kdrive & cw code
COPYING: drop copyright for removed fbmmx.[ch] files
COPYING: drop copyright & license notice for removed fbcompose.c
COPYING: drop copyright for removed kdrive AGP code
COPYING: drop copyright for removed Darwin code in Xquartz
COPYING: drop copyright & license notice for removed i2c multimedia modules
COPYING: remove credit for BSD tsort code
COPYING: add BSD-3-clause license for os/xserver_poll.c
COPYING: add yet another MIT variant for config/fdi2iclass.py
COPYING: add yet another MIT variant for hw/xfree86/parser/InputClass.c
COPYING: add ISC license for os/timingsafe_memcmp.c
COPYING: add BSD-2-clause license for hw/xfree86/common/modeline2c.awk
COPYING: Add NVIDIA/Khronos license for glxvnd server module
COPYING: update copyright dates/holders for remaining existing licenses
COPYING: sort licenses
test/pyxtest: add Solaris equivalent for SO_PEERCRED
test/pyxtest: add test for ProcXIChangeCursor with window None
CI: update FreeBSD image from 14.2 to 15.1
CI: Update debian image to libpciaccess 0.19
xfree86: move pci_device_is_boot_display() fallback to non-exported header
xfree86: correct flag set by AllowForceTerminate option
meson: raise fixesproto required version from 6.0 to 6.1
xkb: Fix -Wcalloc-transposed-args warning in _XkbCopyGeom()
xf86: prevent passing NULL pointer as strcpy destination
xf86: prevent passing NULL pointer as strcat() destination
xf86: silence -Wanalyzer-possible-null-dereference warning in parser
test: silence -Wanalyzer-null-argument warnings in strndup tests
exa: silence -Wold-style-declaration warning from gcc 16
xf86: handle malloc failure in DoSubstitution()
Handle -Wimplicit-fallthrough warnings from gcc 16.1
Drop XWayland DDX
26.1 branch version bump
meson: Change project name to xorg-server
xorg-server 26.0.99.901 (26.1.0 RC1)
Alessandro Bono (1):
ddxLoad: Check XDG_RUNTIME_DIR before fallback to /tmp/
Alex Richardson (3):
Mark the dixChangeWindowProperty() value argument as const
dix/privates.c: Avoid undefined behaviour after realloc()
record: Support architectures with sizeof(void*) > sizeof(long)
Alexander Melnyk (1):
xkb: Fix locked/latched indicator desync across multiple keyboards
Alexander Volkov (2):
ephyr: Send RRCrtcChangeNotify events on resize
dpms: Add support for DPMSInfoNotify event from DPMS 1.2 (xorgproto)
Alexey (1):
Fixed mirrored glyphs on big-endian machines
Andrea Monaco (1):
hw/xfree86/os-support/solaris/sun_vid.c: Fix error message
Andy Myers (2):
xvfb: Add multiple CRTC support
xvfb: Extend -crtcs to accept optional size (N at WxH)
Austin Shafer (12):
xwayland: Move xwl_format array management to its own function
xwayland: Implement linux_dmabuf_feedback event handlers
xwayland: Add get_main_device helper to GBM
xwayland: Add get_drawable_modifiers implementation
xwayland: Make helper for returning a list of formats
xwayland: Return default feedback in xwl_screen
xwayland: Add proper support for telling if a format/mod is supported
dri3: Don't compute intersection with drawable modifiers
xwayland: Send PresentCompleteModeSuboptimalCopy if dmabuf feedback was resent
Add DRM platform for BSD
Add libdrm 2.4.109 requirement
Compile lnx_platform.c on FreeBSD too.
Balló György (2):
glamor: Don't require EXT_gpu_shader4 unconditionally
glamor: Fallback to software rendering on GLSL link failure
Ben Skeggs (1):
xfree86: use modesetting driver by default on GeForce 8 and newer
Benjamin Valentin (1):
xf86: check return value of XF86_CRTC_CONFIG_PTR in xf86CompatOutput()
Benno Schulenberg (1):
xkbUtils: use existing symbol names instead of deleted deprecated ones
Bjarni Ingi Gislason (8):
xorg.conf.man: unprotected period in ellipses
xorg.conf.5: Some formatting and word corrections in the manual
Xserver.man: some minor markup changes
Xserver.man: Fix some textual and formatting issues
Xserver.man: some editorial fixes for the manual
Xserver.man: some remarks and editorial changes for this man page
exa.man: editorial changes for this man page
inputtestdrv.4: editorial changes for this man page
Boris-Barboris (1):
Don't hardcode fps for fake screen
Brian Ruthven (1):
x86emu: re-align breaks in ins() and outs()
Błażej Szczygieł (1):
present: Check for NULL to prevent crash
Chenx Dust (1):
xwayland: fix segment fault in `xwl_glamor_gbm_init_main_dev`
Chia-Lin Kao (AceLan) (1):
hw/xfree86: re-calculate the clock and refresh rate
Christian Göttsche (2):
selinux: remap security classes on policyload
selinux: only generate audit events for avc and error messages
Claes Nästén (1):
xfree86: #ifdef HAS_USL_VTS for switch_to under Solaris
Corentin Noël (1):
glamor: Only check for llvmpipe renderer
Dave Airlie (4):
glamor: add glamor_glsl_has_ints wrapper
glamor: add EXT_gpu_shader4 support
dri2: add crocus to the list of va_gl users
glamor: handle EXT_gpu_shader4 in dual source blend paths
David Jacewicz (1):
xwayland: Aggregate scroll axis events to fix kinetic scrolling
Demi Marie Obenour (7):
Add do-while loops to DIX macros
XFixes: add version check for byteswapped clients
More missing version checks in SProcs
Forbid server grabs by non-WM on *rootless* XWayland
Implement XFixes 6.1
Add AllowForceTerminate to xorg.conf
Add log messages when ForceTerminate is blocked
Diego Viola (3):
Fix typos
Restore correct spelling of "Avance Logic"
treewide: fix typos
Dongwon Kim (2):
modesetting: Correct coordinate info of dirty clips for front-buffer flushing
modesetting: Empty damage once dispatch is done
Doug Brown (1):
dri2: Protect against dri2ClientPrivate assertion failures
Doug Johnson (1):
os: backtrace: Fix -Wincompatible-pointer-types compiler error on 32-bit targets
Doğukan Korkmaztürk (2):
xwayland/glx: Mirror all EGLConfigs
GLX: Free the tag of the old context later
Dr. David Alan Gilbert (1):
xkb: deadcode cleanup
Drew DeVault (1):
Xwayland: implement drm-lease-v1
Edênis Freindorfer Azevedo (1):
Support `XDG Base Dir Spec 0.8`.
Eli Schwartz (1):
meson: fix types for some build options
Enrico Weigelt, metux IT consult (400):
replace _X_INLINE by inline in internal static functions
xkb: drop defining XKBSRV_NEED_FILE_FUNCS
hw: xwayland: fix build if neither gbm nor eglstream available
fix: unused readIntVec()
drop remains of support for old Sun compilers
xfree86: drop remains of old USL compiler
include: os: fix return value of OsLookupColor()
os: oscolor: fix BuiltinColor field naming
os: color: fix possible buffer overflow vulnerability
randr: move private definitons from randrstr.h to randrstr_priv.h
glx: move private definitions from vndserver.h to vndserver_priv.h
xkb: fix int size mismatch
modesetting: fix int size mismatch
xwayland: fix int size mismatch
dix: unexport party_like_its_1989 (retro mode)
factor out X_REGISTRY_RESOURCE and X_REGISTRY_REQUEST to meson.build
dix: dixutils: make workQueue pointer dix-private
dbe: drop obsolete NEED_DBE_PROTOCOL
os: drop unused GetAccessControl()
xfree86: drop unneeded wrapper xf86PrivsElevated()
glamor: glamor_debug.h: drop unused AbortServer() declaration
xkb: drop duplicate _X_EXPORT from .c source
glamor: drop duplicate _X_EXPORT from .c source
xace: drop duplicate export of XaceHooks from .c source
Xi: drop duplicate _X_EXPORT from .c source
randr: drop duplicate _X_EXPORT from .c source
miext: sync: drop duplicate _X_EXPORT from .c sources
dix: drop duplicate _X_EXPORT
xwayland: drop duplicate _X_EXPORT
xfree86: parser: drop HAS_NO_UIDS
include: drop unused including of closure.h
include: drop closestr.h from public module API
os: fix unused variable on non-IPv6 build
os: fix unused variable on WIN32 build
os: fix mising prototype / include on WIN32 builds
xwin: fix unused variables
xwin: winclipboard: fix missing prototypes / missing include
xwin: fix possibly missing string termination
xwin: fix missing prototype for winValidateArgs()
xwin: replace ZeroMemory()
xwin: winsock.h needs to be included earlier
os: simplify win32 uname()
include: move xsha1.h to os/
include: unexport registry.h
drop remains of DMX
os: unexport AutoResetServer()
mi: drop some dead code
os: fix missing X11/Xdefs.h include in os/osdep.h
os: move os_move_fd() out of public API
include: dont install glx_extinit.h
include: unexport xserver_poll.h
xnest: drop superfluous xnestCursorScreenKey define
xnest: fix naming of xnestCursorScreenKeyRec
xnest: use own dev-privates key for per-screen cursor
xfree86: use own dev-privates key for per-screen cursor
dix: drop now obsolete cursorScreenDevPriv
xfree86: os-support: drop unused NO_OSLIB_PROTOTYPES guard
xfree86: os-support: drop unused xf86SerialSendBreak()
Fix missing include of <sys/wait.h>
include: add comment on _XSERVER64 define
xfree86: os-support: drop obsolete Solaris specific LED defines
xfree86: os-support: ppc_video: drop unused DEV_MEM define
xwin: consolidate debugging symbols
Xext: fix missing include of <errno.h>
os: fix missing include of <errno.h>
xquartz: fix missing include of <errno.h>
xwayland: fix missing include of <errno.h>
xfree86: common: fix missing include of <errno.h>
xfree86: os-support: fix missing include of <errno.h>
xfree86: modesettig: fix missing include of <errno.h>
xfree86: int10: fix missing include of <errno.h>
os: rpc: fix type mismatch
meson.build: move manpage specific stuff to man/ subdir
test: simple-xinit: add _X_NORETURN
test: xi2: drop unused variable
os: move SELinux enforcement state to the extension
include: unpexport SELINUX_* consts from include/global.h
config: wscons: use asprintf() instead of deprecated Xprintf()
test: fix deprecated meson calls
config: wscons: fix warning on discarded const
xfree86: modesetting: fix warning on unused variable
test: fix FTBS on missing xlib includes on NetBSD
config: fix wscons backend on NetBSD
xkb: make XkbUpdateKeyTypesFromCore() static
xkb: drop unused defines
xkb: drop never used XkmProbe()
include: xkbstr.h: fix missing include of Xdefs.h
xkb: drop ununsed XkbNameMatchesPattern()
xfree86: os-support: bsd: fix warning on old-style function definition
xfree86: os-support: clean out remains of SVR3/sysv support
xfree86: os-support: drop Solaris pre-7 remains
xfree86: os-support: move _NEED_SYSI86 guarded block to sun_vid.c
xfree86: vgahw: drop obsolete _NEED_SYSI86
present: present_scmd: drop obsolete include of <time.h>
m4: drop autoconf leftovers
os: connection: drop obsolete define Pid_t
xnest: Display: fix xallocarray() compiler warning
Xnest: ignore NoExpose event
Xnest: canonicalize includes: <X11/Xdefs.h>
Xnest: cleanup X.h includes
Xnest: print event ID on warning about unhandled upstream event
xfree86: x86emu: drop unnecessary extern C from debug.h
xfree86: x86emu: fix missing Xfuncproto.h include in debug.h
include: move busfault.h out of public include dir
include: gc.h: drop unused defines
os: unexport xthread_sigmask
os: unexport OsLookupColor()
os: unexport OsVendorVErrorFProc pointer
dix: move closestr.h into dix directory
prevent name clash on Windows w/ RT_* defines
dix: workaround for win32 name clash on CreateWindow()
rename remaining RT_* defines to X11_RESTYPE_*
os: fix missing include of misc.h in busfault.h
os: unexport MakeClientGrabPervious() and MakeClientGrabImpervious()
os: unexport OnlyListenToOneClient()
os: unexport ListenToAllClients()
xfree86: linux: int10: drop dead code
xfree86: drop unused xf86SetReallySlowBcopy()
xfree86: drop unused xf86EnableAGP()
xfree86: os-support: drop ununsed POSIX_TTY
Fix missing include of sys/stat.h
os: unexport ForceClockId()
os: define SECURE_RPC locally instead of global config header
os: secure-rpc: check struct authdes_cred
os: secure-rpc: make build option tristate
xfree86: os-support: bsd: fix warning on discarded const
xfree86: os-support: bsd fix warning on unused label on NetBSD
fix including <sys/mman.h>
xfree86: modes: drop unused xf86_driver_has_show_cursor()
xfree86: x86emu: drop unused ldq_u()
xfree86: x86emu: drop unused stq_u()
xfree86: x86emu: fix warning on unneccessary abs()
xfree86: sdksyms: drop errornous check for mifillarc.h
include: drop obsolete check for typeof operator
include: move dbus-core.h to config
xkb: move *_TIMER defines into xkbAccessX.c
dbe: unexport dbestruct.h
xkb: make XkbInternAtom() static
include: xkbfile: clean up forgotten unused declarations
os: drop remains of STREAMSCONN
record: clean up Sun/Solaris specific hack
kdrive: drop Solaris specific hack
xfree86: common: include math.h unconditionally
xfree86: x86emu: rename segment register fields
os: drop SUN-DES-1 authentication
mi: drop unused XMAJOROCTANTS
mi: drop unused SWAPPT() macro
mi: move *_VISUALS defines into consumer source file
dix: drop unused args from CreateRootCursor()
xnest: don't force it off on Windows
xnest: don't silently disable Xnest
os: access.c: drop unnecessary ifdef
os: drop duplicate nested ifdef TCPCONN
meson: explicitly check whether AF_INET6 is available
os: drop extra ifdefs for AF_INET6
kbd: move _XkbWantsDetectableAutoRepeat() macro into dix/events.c
mi: drop unused miPolyFillRect()
os: move xserver_poll.h into os/ directory
include: dix.h: fix outdated comment
Xext: securitysrv.h: drop hacks for including secur.h
Xext: drop _PANORAMIX_SERVER
xfixes/xace: fix pointer type mismatch on XFixesSelectSelectionInput()
Xace: dont install xace.h and xacestr.h anymore
xace: typesafe hook function for XACE_RESOURCE_ACCESS
xace: typesafe hook function for XACE_DEVICE_ACCESS
xace: typesafe hook function for XACE_SEND_ACCESS
xace: typesafe hook function for XACE_RECEIVE_ACCESS
xace: typesafe hook function for XACE_CLIENT_ACCESS
xace: typesafe hook function for XACE_EXT_ACCESS
xace: typesafe hook function for XACE_SERVER_ACCESS
xace: typesafe hook function for XACE_SCREEN_ACCESS
xace: typesafe hook function for XACE_SCREENSAVER_ACCESS
xace: typesafe hook function for XACE_AUTH_AVAIL
xace: typesafe hook function for XACE_KEY_AVAIL
dix: colormap: fix name clash with win32 api on UpdateColors
Xext: saver: drop New() macro
Xext: saver: little bit formatting cleanup
dix: create empty selection objects as-needed in dixLookupSelection()
fix missing includes of <X11/Xfuncproto.h>
Xext: fix missing include of <X11/Xmd.h>
ci: enable building security extension
xkb: ProcXkbGetGeometry(): fix memleak
meson.build: disable udev on platforms not having it
treewide: replace xnfalloc() calls to XNFalloc()
treewide: replace xnfallocarray() calls by XNFreallocarray
treewide: replace xnfreallocarray macro call by XNFreallocarray()
treewide: replace xnfrealloc() calls to XNFrealloc()
treewide: replace strdup() calls to Xstrdup()
treewide: replace xnfcalloc() calls by XNFcallocarray()
treewide: replace xnfstrdup() calls by XNFstrdup()
xv: drop unused define GLOBAL
xv: drop unused macro _XvBadEncoding
xv: move SCREEN_(PROLOGUE|EPILOGUE) into xvmain.c
xv: move XvVideoNotifyRec into xvmain.c
ci: fix w64 cross build pkg-config path
treewide: mark pGC->ops->CopyArea() calls not using result as void
Xnest: cursor: fix potentially uninitialized memory
Xnest: Keyboard: drop unnecessary include
treewide: fix indentions got broke by recent commit
mi: drop unused miCopyPlane()
mi: drop unused miCopyArea()
mi: drop unused miGetImage()
mi: drop unused miPutImage()
mi: drop obsolete mibitblt.c
doc: drop removed functions from the Xserver spec
os: backtrace: use fixed size array instead of vla
test: dix_input_valuator_masks(): use fixed array instead of VLA
Xnest: add guards to Xnest.h
Xnest: XNGC.h: add missing includes
Xnest: Display.h: fix missing include of colormap.h
Xnest: fix broken exposure events
Xnest: xnestCollectEvents(): scope local variables
Xnest: split off event handler
Xnest: use Xorg's TRUE/FALSE instead of Xlib's True/False
include: dixfontstr.h: drop silent dependency on libxfont2
os: unexport WaitForSomething()
os: utils: minor code formatting cleanup
os: utils: drop unused NO_OUTPUT_PIPES
os: utils: drop REMOVE_LONG_ENV conditional
os: utils: drop unused USE_ISPRINT
os: utils: drop obsolete REMOVE_ENV_LD conditional
include: colormap.h: drop unused typedef colorResourcePtr
include: colormap.h: drop unused defines
dix: move internal defines into colormap.c
include: unexport XIstubs.h
os: unexport CloseDownConnection()
Xext: xf86bigfont: drop some dead code
Xext: xf86bigfont: code styling cleanups
ci: use master branch of xf86-video-qxl driver
ci: add FreeBSD build
ci: reduce nolibdecor build to xwayland only
xfree86: os-support: bsd: fix missing include of xf86_OSproc.h
dix: make CopyGrab() static
dix: make FreeGrab() NULL tolerant
dix: CreateGrab() rename "type" parameter to "eventType"
xfree86: common: xf86Bus: fix char signess mismatch
xfree86: common: xf86Option: fix char signess mismatch
xfree86: common: xf86pciBus: fix char signess mismatch
xfree86: common: xf86Configure: fix char signess mismatch
xfree86: parser: scan: fix char signess mismatch
os: access: fix char signess mismatch
os: utils: fix char signess mismatch
xkb: xkbtext: fix char signess mismatch
xkb: xkbInit: fix char signess mismatch
xkb: drop unused variable extDevReason
xfree86. os-support: drop obsolete XMODE_* defines
xfree86: os-support: drop unused CONSOLE_GET_* defines
xfree86: os-support: move CONSOLE_X_MODE_ON/OFF to bsd_init.c
xfree86: os-support: move CONSOLE_X_TV_ON/OFF to i386_video.c
xfree86: os-support: move including machine/sysarch.h out of public header
xfree86: modesetting: merge FreeRec() into FreeScreen()
xquartz: drop unused code
os: log: use localtime_r() on mingw builds
os.h: drop unnecessary guard on stdlib.h include
os: drop redefining getpid() on mingw32
pseudoramix: replace PseudoramiXTrace & PseudoramiXDebug by LogMessageVerb
Xext: xvmc: drop unused XvMCScreenInitProc
xwin: fix memleak on freeing pixmaps
xfree86: dri: unexport DRIDestroyWindow() and make it static
randr: fix wrong call to RRGetScreenResources() in swapped case
dix: unexport Ones()
glx: drop obsolete glxbyteorder.h
glx: drop obsolete warnings on files being generated
xfree86: parser: drop obsolete token enum values
xfree86: parser: rename IOBASE for fixing name conflict
netbsd: disable pccons support
dix: drop remains of ancient code generator
glx: assign at declaration
glx: DoQueryContext(): use fixed size array instead of variable length
glx: DoQueryContext(): explicitly use reply buf type defined by spec
Xext: geext: drop unused variable extEntry
mi: miline.h: unexport only locally used macros
mi: miline.h: drop DEFAULTZEROLINEBIAS from public header
Xi: fix length checking with bigreq
randr: fix length checking with bigreq
xkb: fix length checking with bigreq
xquartz: fix length checking with bigreq
Xext: saver: fix length checking with bigreq
Xext: security: fix length checking with bigreq
Xext: shape: fix length checking with bigreq
Xext: vidmode: fix length checking with bigreq
Xext: xtest: fix length checking with bigreq
xkb: drop swapping request length fields
xfixes: drop swapping request length fields
composite: drop swapping request length fields
dbe: drop swapping request length fields
record: drop swapping request length fields
pseudoramiX: drop swapping request length fields
present: drop swapping request length fields
render: drop swapping request length fields
randr: drop swapping request length fields
damage: drop swapping request length fields
dri3: drop swapping request length fields
Xext: bigreq: drop swapping request length fields
Xext: dpms: drop swapping request length fields
Xext: panoramiX: drop swapping request length fields
Xext: saver: drop swapping request length fields
Xext: security: drop swapping request length fields
Xext: shape: drop swapping request length fields
Xext: shm: drop swapping request length fields
Xext: sync: drop swapping request length fields
Xext: vidmode: drop swapping request length fields
Xext: xcmisc: drop swapping request length fields
Xext: xf86bigfont: drop swapping request length fields
Xext: xres: drop swapping request length fields
Xext: selinux: drop swapping request length fields
Xext: xtest: drop swapping request length fields
Xext: xv: drop swapping request length fields
Xi: drop swapping request length fields
xfree86: drop swapping request length fields
xquartz: drop swapping request length fields
xwayland: drop swapping request length fields
xwin: drop swapping request length fields
dix: drop swapping request length fields
dbe: drop now obsolete swap procs
randr: drop now obsolete swap procs
Xext: dpms: drop now obsolete swap procs
Xext: panoramiX: drop now obsolete swap procs
Xext: saver: drop now obsolete swap procs
Xext: shape: drop now obsolete swap procs
Xext: shm: drop now obsolete swap procs
Xext: sync: drop now obsolete swap procs
Xext: vidmode: drop now obsolete swap procs
Xext: xcmisc: drop now obsolete swap procs
Xext: xtest: drop now obsolete swap procs
Xext: xv: drop now obsolete swap procs
Xi: drop now obsolete swap procs
xfree86: drop now obsolete swap procs
xfree86: unexport xf86PlatformMatchDriver()
xfree86: common: dont install xf86MatchDrivers.h
xfree86: drop obsolete macro INITARGS
xfree86: vgahw: drop obsolete vgaHWProtectWeak()
xfree86: vgahw: drop obsolete vgaHWBlankScreenWeak()
xfree86: vgahw: make vgaHWRestoreMode() static
xfree86: vgaha: make vgaHWRestoreColormap() static
xfree86: vgahw: make vgaHWSaveMode() static
xfree86: vgahw: make vgaHWSaveColormap() static
xfree86: vgahw: drop obsolete vgaHWSetRegCounts
xfree86: vgahw: drop obsolete vgaHWDisable()
xfree86: vgahw: drop obsolete vgaHWSaveScreenWeak()
meson: drop defining BIGREQS
Xext: saver: fix missing swap in QueryVersion reply
Xext: saver: consolidate (non-)xinerama versions
mi: miexpose: fix FTBS w/ rootless helper
miext: rootless: fix unused variables
ci: workaround for building xf86-video-intel via autotools
ci: add intel driver to build matrix
xfree86: xf86Opt.h: fix missing include
os: drop `upstart` specific SIGSTOP signaling logic
os: no need to defined PATH_MAX
xfree86: os-support: unexport xf86scanpci()
modsetting: also add libglx to library symbol test
dri: report failed memory allocation
doc: drop removed PaintWindowBackground() and PaintWindowBorder()
xfree86: xf86configure: use NULL instead of 0
glamor: use explicit field initializers for XF86ModuleData
xfree86: fbmodule: use explicit field initializers for XF86ModuleData
xfree86: glxmodule: use explicit field initializers for XF86ModuleData
xfree86: sfbmodule: use explicit field initializers for XF86ModuleData
xfree86: shmodule: use explicit field initializers for XF86ModuleData
xfree86: vgaHWmodule: use explicit field initializers for XF86ModuleData
xfree86: xfbmodule: use explicit field initializers for XF86ModuleData
xfree86: xf86int10module: use explicit field initializers for XF86ModuleData
xfree86: fbdevhw: use explicit field initializers for XF86ModuleData
xfree86: exa: use explicit field initializers for XF86ModuleData
xfree86: modsetting: use explicit field initializers for XF86ModuleData
xfree86: inputtest: use explicit field initializers for XF86ModuleData
xfree86: doc: update docs on XF86ModuleData
ci: update freebsd builder image
xfree86: modesetting: don't use VLA
test: sync: don't use VLA
meson.build: enable VLA warning
present: need to include dix-config.h
present: need to include <X11/Xfuncproto.h>
glamor: don't need NULL check before free()
xwin: don't need NULL check before free()
Xext: geext: drop unused GEEventFill() macro
Xext: geext: drop unused GEIsType() macro
Xext: geext: drop unused GECLIENT() macro
Xext: geext: drop unused GEMaskIsSet() macro
Xext: geext: drop unused GEEXTIDX() macro
Xext: geext: drop unused GEEXT() macro
Xext: geext: drop unused GEV() macro
Xext: geext: unexport GEExtensions[]
Xext: geext: move struct _GEExtension into geext.c
Xext: geext.h: fix missing include of Xfuncproto.h
present: fix prototype for present_select_input()
dbe: fix byte swapping in SProcDbeSwapBuffers()
present: need to include geext.h
Xext: dpms: need to include geext.h
drop not needed includes of geext.h
os: let vpnprintf() accept %X
xfree86: xf86helper: fix NULL dereference
xfree86: platform_noop: add missing functions
xfree86: os-support: fix FTBS when no recent enough libdrm found
Xnest: use authorative declarations from X11/XKBlib.h
ci: fix missing runner tag on FreeBSD jobs after gitlab migration
kdrive: Xkdrive.man: remove stray whitespace
xwayland: no need to use WriteReplyToClient()
randr: fix unconditional byte-swap in ProcRRGetProviderInfo()
Eric Curtin (1):
config: add a quirk for Apple Silicon appledrm
Erik Kurzinger (13):
xwayland: correctly report PresentCompleteModeCopy
xwayland: add detection for drivers that don't support implicit sync
Update CI for Xwayland explicit sync
DRI3: provide stub implementation of DRI3SetDRMDeviceInUse
DRI3: add DRI3ImportSyncobj and DRI3FreeSyncobj
xwayland: add functions to import and export dma-buf implicit fences
xwayland: re-compute target msc during xwl_present_re_execute
Present: add PresentCapabilitySyncobj and PresentPixmapSynced
xwayland: support DRI3 1.4 and Present 1.4
xwayland: add support for wp_linux_drm_syncobj_v1
xwayland: don't scrap pending present requests
xwayland: use write fence in xwl_glamor_dmabuf_import_sync_file
present: signal explicit sync release point in present_vblank_scrap
Faith Ekstrand (1):
glamor: Enable dma-buf on Zink
FeepingCreature (1):
xkb: Avoid length-check failure on empty strings.
Florian Weimer (2):
fb: Declare wfbFinishScreenInit, wfbScreenInit for !FB_ACCESS_WRAPPER
xwayland: Use correct pointer types on i386
Fotios Valasiadis (1):
os: Explicitly include X11/Xmd.h for CARD32 definition to fix building on i686
Gary T. Giesen (2):
config/udev: guard against NULL subsystem in fallback bus id
xfree86: set GPU screen FB/DGA defaults on runtime hotplug
Gleb Popov (2):
Implement -novtswitch option handling for FreeBSD.
The framebuffer driver on FreeBSD is called scfb, use it.
Ian Douglas Scott (1):
xwayland: Release keys on keyboard `enter` event if `leave` wasn't received
Ian Forbes (1):
xwayland: Try harder to find a top-level for root grabs
Icenowy Zheng (3):
glamor: Fix dual blend on GLES3
modesetting: properly use fb_id of front_bo for reverse PRIME CRTC
randr: do full transform when checking SetScreenSize size
Ignacio Casal Quinteiro (1):
touchevents: set the screen pointer after checking the device is enabled
Ilya Pominov (1):
RandR: Allow duplicate monitor name when adding it
Ivan A. Melnikov (1):
glamor: Don't initialize on softpipe
Ivaylo Dimitrov (1):
linux: Fix BUS_PLATFORM detection for non-PCI devices
Izumi Tsutsui (3):
Revert "fb: Remove even/odd tile slow-pathing"
Revert "xfree86: Remove -flippixels"
fb: Fix 1bpp Xservers on "whitePixel=0, blackPixel=1" VRAMs
James Jones (1):
Use EGL_LINUX_DMA_BUF_EXT to create GBM bo EGLImages
Jan Beich (4):
xwayland: add missing dependency on xwaylandproto
os: Use LOCAL_PEERCRED to determine local client PID on FreeBSD
os: Use KERN_PROC_ARGS to determine client command on DragonFly and FreeBSD
xwayland: avoid Linux-only headers on non-Linux
Jan Engelhardt (1):
glamor: explicitly draw endpoints of line segments
Jeffy Chen (1):
glamor: xv: Fix invalid accessing of plane attributes for NV12
Jeremy Huddleston Sequoia (66):
rootless: Dead code removal (ROOTLESS_REDISPLAY_DELAY is already defined)
X11Application: Ensure TIS operations are done on the main thread
os/connection: Improve abstraction for launchd secure sockets
xquartz: Create a separate category for organizing user preferences
xquartz pbproxy: Adopt NSUserDefaults+XQuartzDefaults for preferences
xquartz: Fold spaces related preferences into NSUserDefaults+XQuartzDefaults
XQuartz: Ensure scroll events are delivered to a single window (not both X11 and AppKit)
meson: Bump requirement to meson-0.50.0
xquartz: Update Sparkle configuration to use SUPublicEDKey
xquartz: Update copyright for 2022
meson: Provide options to set CFBundleVersion and CFBundleVersionString in XQuartz
Revert "meson: Bump requirement to meson-0.50.0"
print_edid: Fix a format string error
xf86-input-inputtest: Fix build on systems without SOCK_NONBLOCK
tests: Fix build failure from missing micmap.c
meson: Support building Xnest and Xorg on darwin
XQuartz: Build the bundle trampoline when using meson
XQuartz: Add TCC reason keys to Info.plist
xquartz: Use correct defines when building to support Sparkle updates
meson: Use system method for locating tirpc
CI: Update to xcb-proto-1.14.1 to support python 3.9
CI: Use -fcommon to build libX11 for mingw
CI: Use -fcommon to build xtst
CI: Update gitlab CI to use debian bullseye
meson: Bump requirement to meson-0.52.0
xquartz: Fix a possible crash when editing the Application menu due to mutaing immutable arrays
XQuartz: Improve type safety for X11Controller's application menu editor
xquartz: Remove unused macro (X11LIBDIR)
xquartz: Move default applications list outside of the main executable
meson: Don't build COMPOSITE for XQuartz
xquartz: Fix some formatting
xquartz: Ignore SIGPIPE at process launch
xquartz: Use xorg_backtrace() instead of rolling our own for debugging
rootless: Add additional debug logging to help triage XQuartz fb/rootless/damage crashes
dix: Stop recycling scratch pixmaps
dix: Remove pScratchPixmap and other associated ABI changes
xquartz: Update the about box copyright to 2023
xquartz: Disable COMPOSITE at runtime
Revert "meson: Don't build COMPOSITE for XQuartz"
rootless: Fixup some format errors in debug logging
rootless: Remove option to disable ROOTLESS_RESIZE_GRAVITY
rootless: Ensure gResizeDeathPix is stored in locally-managed memory rather than re-using the implementation's backing store
rootless: Use RL_GRAVITY_NORTH_WEST for min/max/zoom resizing
rootless: Remove the special case for northwest gravity in StartFrameResize
rootless: Dead code removal (resize_after in StartFrameResize / FinishFrameResize)
rootless: Remove an unnecessary memory copy when handling resize with gravity RL_GRAVITY_NONE (border width changes)
rootless: Dead code removal (RootlessResizeCopyWindow)
rootless: Use screen_x and screen_y instead of pixmap pointer hacks
os: Update AllocNewConnection() debug logging to include whether or not the client is local
os: Update GetLocalClientCreds to prefer getpeerucred() or SO_PEERCRED over getpeereid()
os: Use LOCAL_PEERPID from sys/un.h if it is available to detemine the pid when falling back on getpeereids()
darwin: Implement DetermineClientCmd for macOS
rootless: Fix Glyphs damage bounding box to correctly compute union
rootless: Add Trapezoids, Triangles, and CompositeRects wrapping
rootless: Protect alpha channel for Render operations
xquartz: Bump copyrights in Info.plist to 2026
xquartz/GL: silence OpenGL deprecation warnings
xquartz/GL: advertise GLX_ARB_create_context and _profile
xquartz: Activate the app via xp_window_activate() in -set_front_process:
xquartz/GL: Log failures on the indirect GLX make-current path
fb: Don't widen the planemask over padding bits when ROOTLESS_SAFEALPHA is set
meson: fix xquartz_data_dir path construction
xquartz: Stop drawing before handing a frame to xp_frame_draw()
darwin: Set thread priorities to user interactive or user initiated as appropriate
rootless: Fix two region leaks
rootless: Keep the screen pixmap header consistent with its allocation
Jessica Clarke (4):
xwayland: Avoid gratuitous round trip through event_id
xwayland: Pass vblank pointer itself to xwl_present_flip
xwayland: Stop relying on event_id being a valid pointer
xwayland: Stop using event address as event_id
JiangWu (1):
randr: Correctly get physical size for screen with RandR 1.5
Joaquim Monteiro (2):
os: Fix assignment with incompatible pointer type
os: Fix siHostnameAddrMatch in the case where h_addr isn't defined
Jocelyn Falempe (5):
xf86/logind: fix call systemd_logind_vtenter after receiving drm device resume
xf86/logind: Fix drm_drop_master before vt_reldisp
xf86/logind: Fix compilation error when built without logind/platform bus
xf86/logind: fix missing call to vtenter if the platform device is not paused
x86/logind fix suspend/resume when there are no input devices
John D Pell (1):
XQuartz: stub: Call LSOpenApplication instead of fork()/exec()
John Kennedy (2):
Extented 'arm' case to 'aarch64' on BSD.
Enable USE_DEV_IO on FreeBSD/aarch64
Jon Turney (11):
Fix compilation with windows.h from latest w32api
Don't underlink inputtest on targets which require complete linkage
s/__/@/ in inputtestdrv manpage
meson: Add dependencies for hw/xwin/ resource compilation
meson: Correctly set Libs: in xorg-server.pc for Windows
meson: Fix build of xwinclip tool when xcb is installed in non-default location
appveyor: Add libxcvt build dep
hw/xwin: Use revert-to-parent X focus mode in multiwindow WM
hw/xwin: Always set the X input focus to none when an X window loses focus
hw/xwin: More adjustments to multiwindow mode focus handling
hw/xwin: Allow DefWindowProc to SetFocus() as needed after WM_ACTIVE
Jonas Ådahl (6):
xwayland/glamor/gbm: Only use modifier gbm API if explicit
xwayland/glamor/gbm: Initialize explicit buffer params in helper
xwayland/glamor/gbm: Use helper for implicit buffer params too
xwayland/glamor: Track if a xwl_pixmap uses explicit modifiers
xwayland/window: Move set-allow functions lower down
xwayland/window: Queue damage after commits are allowed
Jonathan Gray (1):
glamor: fix free of uninitialised pointers
Joshua Ashton (8):
xwayland: Add some more xwayland fake modes
xwayland: Add -force-xrandr-emulation switch
ci: Bump to wayland 1.21.0
ci: Bump to wayland-protocols 1.28 for xwayland_shell
xwayland: Implement xwayland_shell_v1
xwayland: Don't expose XRandR emulated modes for leaseable displays
glamor: Don't glFlush/ctx switch unless any work has been performed
xwayland: Send ei_device_frame on device_scroll_discrete
José Expósito (6):
test: Use Xwayland instead of wayland/weston-info
test: Xwayland doesn't start when another X server is running
xwayland/glamor/gbm: Set GBM_BO_USE_LINEAR if only LINEAR modifier is supported
Xi: do not keep linked list pointer during recursion
ephyr: Fix incompatible pointer type build error
xkb: Check that needed is > 0 in XkbResizeKeyActions
Julian Orth (4):
os/connection: don't leave `port` uninitialized
xwayland: copy repeat settings from the compositor map
xwayland: Don't run key behaviors and actions
xwayland: don't allow clients to modify the keymap
Kenny Levinsen (4):
xwayland: Commit after acknowledging configure
xwayland: Make xwl_window_libdecor_resize reusable
xwayland: Apply root toplevel configure dimensions
xwayland: Default geometry for undecorated rootful
Konstantin (27):
meson: add glamor gles2 tests
glamor: make use of GL_EXT_texture_format_BGRA8888
glamor: transpose gradients transparently
glamor: fix XVideo run with GLES
glamor: fixes GL_INVALID_ENUM errors on ES if there is no quads
glamor: add gl_PointSize for ES shaders
glamor: require GLES 2.0 on GL ES CI
tests: enable CI for both GLES2 and GLES3 variants
glamor: mark tests fixed by this PR
xwayland/glamor/gbm: use GBM_FORMAT_ARGB8888 for 24-bit on ES
glamor_egl: add helper functions for contexts
glamor_egl: add RenderingAPI option
glamor_egl: add info message about context API
xorg.conf.man: document new RenderingAPI option
hw/Xwayland: add xwl_glamor_mode_flags enum
Xwayland: add "glamor" command line option
Xwayland: document new "glamor" option
Xwayland: add new "have_glamor_api" pkgconfig
glamor_egl: add support of GlxVendorLibrary option
Revert "glamor/glxprov: Stop exposing non-db(-capable) configs"
glamor: xv: do not force a version on XV shaders
glamor: xv: reuse ports and shaders when possible
glamor: xv: prepare to one-plane formats
glamor: xv: enable UYVY acceleration
glamor: check BPP by render_format.
glamor: xv: fix UYVY alignment
xv: change FOURCC_RGBA32 to AMD one
Konstantin Kharlamov (9):
exa: fix "comparison is always false"
xfree86: numTimings is never value other than 0
Xext: the check firstValuator ≤ 1 is duplicated in this branch
xkbtext: fix copy-paste error
glx: remove a noop assert (index is unsigned)
modesetting: don't pass a big struct by value
fdi2iclass.py: use "is" to compare with None
fdi2iclass: remove unused local variable
gen_gl_wrappers: remove unused imports
Konstantin Pugin (5):
glamor: support GLES3 shaders
glamor: accelerate incomplete textures for GL ES
glamor: add glvnd_vendor private
xorg: initialize glamor provider
Xephyr: use glamor glx provider
Leon M. Busch-George (1):
xwayland/glamor/gbm: get_render_node_path without enumeration
Liu Heng (2):
xwayland: Fix incorrect pointer coordinates in enter events
xwayland: prevent X11 get enter event when pointer is over Wayland client
Luc Ma (1):
ci: remove redundant slash in libxcvt repository url
Lucas Stach (4):
xwayland: handle fd export failure in glamor_egl_fds_from_pixmap
xwayland: properly get FDs from multiplanar GBM BOs
glamor_egl: handle fd export failure in glamor_egl_fds_from_pixmap
glamor_egl: properly get FDs from multiplanar GBM BOs
Luke Dashjr (1):
Xvfb: Support up to 13 mouse buttons
Marek Marczykowski-Górecki (1):
Xephyr: fix setting physical output size
Mario Kleiner (11):
modesetting: Fix VRR window property handling.
Revert "glamor: Enable modifier support for xfree86 too"
modesetting: Allow Present flips with mismatched stride on atomic drivers.
modesetting: Add option for non-vsynced flips for "secondary" outputs.
xfree86: Avoid crash in xf86RandR12CrtcSetGamma() memcpy path.
xfree86: Let xf86RandR12CrtcComputeGamma() deal with non-power-of-2 sizes.
Revert "modesetting: Only use GAMMA_LUT if its size is 1024"
modesetting: Enable GAMMA_LUT for lut's with up to 4096 slots.
modesetting: Handle mixed VRR and non-VRR display setups better.
modesetting: Consider RandR primary output for selectioh of sync crtc.
Fix RandR leasing for more than 1 simultaneously active lease.
Mario Limonciello (3):
Add check for `pci_device_linux_sysfs_boot_display()`
Add compatibility define for `pci_device_is_boot_display()`
xfree86: prefer boot_display over boot_vga for primary device
Mario Limonciello (AMD) (1):
Disable pciaccess for mingw
Martin Burggraf (1):
xkb: correcting mathematical nonsense in XkbGeomFPText
Martin von Gagern (1):
modesetting: Check for NULL mode_output before printing warning message
Matt Turner (4):
Build xz tarballs instead of bzip2
test: #undef NDEBUG so assert is not compiled away
hw/xfree86: Fix -Wmissing-prototypes warnings
hw/xfree86: Fix -Wincompatible-pointer-types sbus compile failure
Matthieu Herrb (16):
Make xf86CompatOutput() return NULL when there are no privates
Initialize Mode->name in xf86CVTMode()
Better fix for xf86CompatOut() when there are no privates
remove the PRE_RELEASE message.
Convert more funcs to use InternalEvent.
Fix build on OpenBSD.
Add full prototypes in hw/xfree86/os-support/bsd/bsd-video.c
xfree86/bsd: fix build on NetBSD/amd64.
OpenBSD build fix: struct ucred is struct sockpeercred there
bsd_init.c: fix build on OpenBSD
present: On *BSD, epoll-shim is needed to emulate eventfd()
Don't crash if the client argv or argv[0] is NULL.
Return NULL in *cmdname if the client argv or argv[0] is NULL
Fix a double-free on syntax error without a new line.
xkb: Fix buffer overflow in _XkbSetCompatMap()
Fix drmModeCreatePropertyBlob() length parameter after f894801fa20c
Maya Rashish (1):
Simplify auto device configuration for choosing wsfb, fbdev
Michael Dluhosch (1):
xkb: Replaced hardcoded values with compile time options
Michael Wyraz (1):
Removing the code that deletes an existing monitor in RRMonitorAdd
Michel Dänzer (164):
randr: Bail from RRTellChanged if there's no root window yet
xwayland: Call RRTellChanged if the RandR configuration may have changed
xwayland/eglstream: Consolidate pending_cb destruction
xwayland/eglstream: Drop xwl_eglstream_set_window_pixmap
present: Pass capabilities to present_vblank_create by value
present: Remove create_event_id hook
present: Dispatch clear_window_flip via present_screen_priv hook
present: Move present_wnmd_screen_init to present_wnmd.c
present: Fold wnmd_init_mode_hooks into wnmd_screen_init
present: Move present_wnmd.c contents to hw/xwayland/xwayland-present.c
xwayland/present: Fold present_wnmd_screen_init into xwl_present_init
xwayland/present: Fold present_wnmd_flip into present_wnmd_execute
xwayland/present: Drop present_wnmd_flush in favour of xwl_present_flush
xwayland/present: Fold present_wnmd_abort_vblank into its only caller
xwayland/present: Simplify query_capabilities
xwayland/present: Fold present_wnmd_check_flip into its callers
xwayland/present: Fold present_wnmd_get_crtc into present_wnmd_pixmap
xwayland/present: Fold present_wnmd_queue_vblank into its callers
xwayland/present: Fold present_wnmd_get_ust_msc into its callers
xwayland/present: Merge present_wnmd_flips_stop & xwl_present_flips_stop
present: Remove present_wnmd_info_rec
xwayland/present: Rename present_wnmd_* functions to xwl_present_*
xwayland/present: Simplify calls to Xwayland-private functions
xwayland/present: Drop abort member of struct xwl_present_event
present: Refactor present_vblank_init helper ouf of _vblank_create
xwayland/present: Embed present_vblank_rec in xwl_present_event
xwayland/present: Fold xwl_present_flip_notify into its callers
xwaland/present: Drop flip_pending member of struct xwl_present_window
xwayland/present: Drop sync_flip member of struct xwl_present_window
xwayland/present: Fold xwl_present_idle_notify into its caller
xwayland/present: Use exec_queue for deferring completion events
xwayland/present: Fold xwl_present_event_notify into its caller
xwayland/present: Drop exec_queue member from struct xwl_present_window
xwayland/present: Drop list member from struct xwl_present_event
xwayland/present: Drop pending member from struct xwl_present_event
xwayland/present: Drop target_msc member from struct xwl_present_event
xwayland/present: Fold xwl_present_release_event into _free_event
xwayland/present: Use present_vblank_ptr instead of xwl_present_event*
present: Drop flip_idler member from present_vblank_rec
xwayland/present: Move xwl_present_reset_timer call out of xwl_present_flip
xwayland: Store EGLContext pointer in lastGLContext
Fix spelling of Xwayland
xwayland/present: Run fallback timer callback after more than a second
xwayland/glx: Flip order of sRGB & non-sRGB fbconfigs
xwayland: Clear timer_armed in xwl_present_unrealize_window
xwayland: Always hook up frame_callback_list in xwl_present_queue_vblank
xwayland/present: Do not send two idle notify events for flip pixmaps
xwayland: Add break statements in pointer_handle_axis
ci: Include meson logs in build job artifacts
ci: Always generate artifacts from build jobs
test: Fix 'xephr' mis-spelling
test: Exclude two XTS xsetfontpath tests
ci: Install weston from Debian
ci: Use fixed Git commits for piglit, rendercheck & xts
ci: Move build job script to a separate file
ci: Check that all expected piglit results are there
dix: Skip more code in SetRootClip for ROOT_CLIP_INPUT_ONLY
ci: Use "meson test" instead of "ninja test"
ci: Move dist testing to a separate job
ci: Export LP_NUM_THREADS=0 for meson test
xwayland: Spell Xwayland consistently in error messages
xwayland: Spell XWAYLAND consistently in debug messages
xwayland: Do not use "XWayland" spelling in code identifiers
xwayland: Refactor xwl_present_for_each_frame_callback helper
xwayland: Prevent nested xwl_present_for_each_frame_callback calls
xwayland/glamor/gbm: Use EGL_NO_CONTEXT with EGL_NATIVE_PIXMAP_KHR
glamor: Remove unused transfer functions
glamor: Make program APIs take DrawablePtrs instead of PixmapPtrs
glamor: Take DrawablePtr instead of PixmapPtr in up/download_boxes
glamor: Eliminate glamor_fini_pixmap
glamor: glamor_prep_pixmap_box → glamor_prep_drawable_box
glamor: Fix up alpha channel if needed in glamor_upload_boxes
glamor: Use DrawablePtr in struct copy_args
composite: Free cs->implicitRedirectExceptions in compCloseScreen
composite: Expose CompositeIsImplicitRedirectException
xwayland/glamor: Require equal pixmap depths in xwl_glamor_check_flip
xwayland/glamor: Avoid implicit redirection with depth 32 parent windows
glamor: Add and use glamor_drawable_effective_depth helper
mi: Fix up alpha channel if needed in miPaintWindow
glamor: Make glamor_solid_boxes take a DrawablePtr
xwayland/glamor: Avoid implicit redirection with depth 32 parent windows
glamor: Ignore destination alpha as necessary for composite operation
xwayland/present: Handle NULL window_priv in xwl_present_cleanup
test: Wait only up to 5 seconds for weston to start up
test: Kill weston whenever shell exits
test: Propagate Xwayland stdout/stderr output and exit status
test: Skip Xwayland test early if PIGLIT_DIR / XTEST_DIR isn't set
ci: Prevent duplicate pipelines for MRs
glamor: Don't override source alpha to 1.0 if it's used for blending
xwayland: Make copy_pixmap_area return void
xwayland: Rename helper to xwl_window_buffer_maybe_dispose
xwayland: Drop xwl_window_buffers_recycle
xwayland: Use window pixmap as a window buffer
xwayland: Return NULL from xwl_window_buffer_get_available
glamor: Make glamor_set_alu take a DrawablePtr
glamor: Fall back for mixed depth 24/32 in glamor_set_alu
xwayland: Destroy old window pixmap in xwl_window_recycle_pixmap
xwayland: Update screen pixmap for root window in xwl_window_set_pixmap
xwayland/present: Update screen pixmap in xwl_present_execute
xwayland: Initialize Present extension support also with rootful
xwayland: Handle NULL xwl_pixmap in xwl_shm_pixmap_get_wl_buffer
xwayland: Add xwl_pixmap_get_wl_buffer helper
xwayland: Enable Present extension support also without glamor
ci: Create check-merge-request job only in MR pipelines
xwayland: Use border width in xwl_glamor_gbm_create_pixmap_for_window
xwayland: Do not plumb damage region through function parameters
xwayland: Call xwl_window_buffer_add_damage_region from damage_report
xwayland: Rename xwl_window_recycle_pixmap to xwl_window_realloc_pixmap
xwayland: Refactor xwl_window_swap_pixmap out of _buffers_get_pixmap
xwayland: Re-use xwl_window_realloc_pixmap in xwl_window_swap_pixmap
xwayland: Replace window pixmap as needed for drawing operation
xwayland/present: Handle clearing damage after flip in xwl_present_execute
ci: Make test stage jobs not depend on earlier stage jobs
xwayland: Use xwl_window for tracking focus/touch
xwayland: Rename xwl_window::window to ::toplevel
xwayland: Return struct xwl_window * from ensure_surface_for_window
xwayland: Call register_damage depending on ensure_surface_for_window
xwayland: Use xwl_window for damage closure
xwayland: Pass xwl_window to xwl_glamor_dri3_syncobj_passthrough
xwayland: Add xwl_window::surface_window
xwayland: Use ConfigNotify screen hook instead of ResizeWindow
xwayland/present: Add xwl_present_maybe_(un)redirect_window
xwayland: Add SourceValidate hook
xwayland/present: Check window & source pixmap depth match last
xwayland/present: Redirect surface window as needed for page flips
xwayland: Call drmFreeDevice for dma-buf default feedback
xwayland: Use drmDevicesEqual in xwl_dmabuf_feedback_tranche_done
dri3: Free formats in cache_formats_and_modifiers
xwayland/glamor: Handle depth 15 in gbm_format_for_depth
xwayland/present: Skip queued flip when a new one becomes ready
xwayland/present: Drop vblank->flip_ready assignment
xwayland: Drop pixmap parameter from xwl_present_maybe_redirect_window
xwayland: Only ignore manual redirection by clients for surface window
xwayland: Try manual redirection for surface window in glamor_check_flip
xwayland/glamor: Try manual redirect only if parent window has depth 32
xwayland/present: Update surface window again if manual redirect fails
xwayland/glamor/gbm: Don't close fence_fd after xwl_glamor_wait_fence
xwayland/present: Check allow_commits in xwl_present_flip
xwayland/glamor: Drop expecting_event bailing from xwl_drm_handle_device
xwayland: Always decrement expecting_event in xwl_output_create
xwayland/glamor: Clean-up GBM's screen private on failure
ci: Install XCB dependencies for meson tests
xwayland/present: Only flip if the window pixmap dimensions match
xwayland: Take viewport scale into account for the input region
xwayland: Add heuristic for WM windows based on reparenting
xwayland: Ignore non-InputOutput children in window_get_client_toplevel
xwayland: Use separate comment for each xwl_output_fake_modes line
xwayland: Sort xwl_output_fake_modes entries
xwayland: Use logical_ prefix for logical coordinate system values
xwayland: Refactor output_get_logical_mode/extents helpers
xwayland: Set output mode size as reported by the wl_output protocol
xwayland: Do not assume the first RandR mode is the logical mode
xwayland: Add RandR mode for the native resolution if it fits in logical
xwayland: Clear ConstrainCursorHarder in xwl_screen_init_output
xwayland: Add emulated modes larger than the logical mode
xwayland: Adjust RandR emulation for rotation
Revert "composite: Only copy bits from the parent pixmap when absolutely necessary"
composite: Skip copying parent pixmap contents when possible
xwayland: Update surface window from xwl_unrealize_window
xwayland: Use WindowPtr for damage closure again
Revert "xwayland: Call register_damage depending on ensure_surface_for_window"
xwayland: Handle GetCurrentClient returning NULL in xwl_reparent_window
dri2: Use booleans for (fake) front buffer tracking in do_get_buffers
dri2: Deduplicate attachments in do_get_buffer
Mike Blumenkrantz (1):
xwayland: connect to the wl display before calling into EGL
Mike Gorse (1):
dix: Use CopyPartialInternalEvent in EnqueueEvent
Mikhail Dmitrichenko (14):
xwayland: Fix search of duplicate lease names
os: avoid potential out-of-bounds access at logVHdrMessageVerb
dix: avoid null ptr deref at doListFontsWithInfo
os: avoid closing null fd at Fopen
render: fix multiple mem leaks on err paths
dix: avoid null ptr deref at doListFontsAndAliases
xkb: fix incorrect size check when growing doodads in a section
vfb: use snprintf when writing XWD window name
xkb: fix potential buff overflow in XkbVModIndexText for XkbCFile format
composite: fix potential mem leak in PanoramiXCompositeNameWindowPixmap
glx: use XNFcallocarray for DRI config allocation
xwayland: check queued DRM lease allocation
os: check ospoll allocation failures
xkb: preserve buffer on realloc failure
Minh Phan (3):
randr: introduce rrCrtcGetInfo DDX function
xwayland/output: properly return the current emulated mode when queried
xwayland/window: Do not double add window to damage list
Moritz Bruder (1):
fbdevhw: Support symbolic links in fbdev_open
Morose (1):
xwayland: Fix check logic in sprite_check_lost_focus()
Nathan Kidd (2):
glx: Fix out-of-bounds reads from negative return
glx: Don't blindly write 8 bytes in GLX single replies
NetSysFire (1):
xorg.conf.man: Fix escape sequence typo
Niclas Zeising (1):
Extend Linux #ifdef to FreeBSD OS.
Nicolas Dufresne (1):
glamor: xv: Rewrite UYVY shader to match NV12/I420 CSC
Nicolas Guichard (1):
xwayland: Fix minimum wl_compositor protocol version
Octavia Togami (1):
Fix use-after-free caused by duplicate glyphs in one glyphset
Olivier Fourdan (309):
ci: Install libxcvt from git
build: Add dependency on libxcvt
xwayland: Use libxcvt
xfree86: Use libxcvt
xfree86/cvt: Drop cvt utility
xfree86: Move xf86CVTMode() function
xwayland: Fix leak of xwl_screen on init
xwayland: Fix memory allocation test
glamor: Fix leak in glamor_build_program()
xwayland/shm: Avoid integer overflow on large pixmaps
xwayland: Set GLVND driver based on GBM backend name
xwayland: Notify of root size change with XRandR emulation
xwayland: Clear tablet cursor pending frame cb
xwayland/test: Don't catch errors in run-piglit.sh
xwayland: Rename xwl_seat_update_cursor()
xwayland: Move xwl_cursor_release() to xwayland-cursor.c
xwayland: Add xwl_cursor_clear_frame_cb()
xwayland/eglstream: Demote EGLstream device warning
xwayland/glamor: Change errors to verbose messages
xwayland/glamor: Log backend selected for debug
xwayland/eglstream: Prefer EGLstream if available
xwayland: Raise the FD limit to the max
render: Fix build with gcc 12
xwayland: Fix cursor color
Xwayland: Do not map the COW by default when rootless
xwayland/present: Fix use-after-free in xwl_unrealize_window()
randr: No need to check RRGetOutputProperty() twice
randr: Add "RANDR Emulation" property
xwayland/output: Set the "RANDR Emulation" property
xwayland: catch SetWindowPixmap() even when rootful
xwayland: make the output serials belong to the screen
xwayland: update_screen_size() takes a screen argument
xwayland: add a fixed geometry size for rootful
xwayland: add xwl_output_from_wl_output()
xwayland: keep track of the wl_output enter/leave
xwayland: keep the xdg_toplevel around
xwayland: pass the emulated mode by reference
xwayland: update the Xwayland screen size first
xwayland: add fullscreen mode for rootful
xwayland: do not auto-lock pointer when rootful
xwayland: add (fake) device grab support
xwayland: move the root window surface to its own function
xwayland: set the surface title when running rootful
xwayland: add xdg-toplevel listener
xwayland: set the app_id and install a desktop launcher
xwayland: set tag on our surfaces
xwayland: add optional support for libdecor
ci: add libdecor
xwayland: Fix "-force-xrandr-emulation"
dix: Fix overzealous caching of ResourceClientBits()
xwayland: Prevent Xserver grabs with rootless
xwayland: Delay wl_surface destruction
xwayland: Clear the "xwl-window" tag on unrealize
build: Bump wayland requirement to 1.18
xwayland/input: Do not ignore leave events
modesetting: Document the "Atomic" option
modesetting: Log whether atomic modesetting is enabled
xfree86: Fix videodrv ABI version
xwayland: Commit surface changes with libdecor configure
build: Bump Wayland dependency to 1.21
xwayland: wl_pointer.axis_v120 is no longer optional
dix: Clear device sprite after free in AttachDevice()
xwayland: Tell RR has changed only when done
xwayland: Use xdg-output name for XRandR
xwayland: Pass the wl_output version
xwayland: Use wl_output.name for XRandR
xwayland: Include <sys/type.h> where needed
xwayland: Use MAP_PRIVATE for keymaps
xwayland: Fix uninitialised value created by a stack allocation
test: Use either wayland-info or weston-info
composite: Fix use-after-free of the COW
xwayland: Use a dedicated feedback callback for windows
xwayland: Check for scanout support in tranches
xwayland: Check for implicit scanout availability
xwayland: Add a direct hook to create pixmaps with glamor
xwayland: Add create_pixmap_for_window() to GBM backend
xwayland: Create scanout capable BO with the fallback path
xwayland: Try the Xwayland glamor hook to create pixmaps
xwayland: Recycle buffers when dmabuf feedback changes
xwayland: Make Wayland logs non-fatal
glamor: Fix build without GBM
xwayland: Fix build without GBM
xwayland: Add xwl_glamor_get_drawable_modifiers_and_scanout()
xwayland: Use the new API to set scanout
xwayland: Do not round non-standard modes
xwayland: Use our CVT function for fixed mode as well
xwayland: Fix spelling of modeinfo in function name
xwayland: Keep the CVT timings for non-standard modes
input: Add new hook DeviceSendEventsProc for XTEST
xwayland: Fallback to plain XTEST if EI does not work
xwayland: Make xwl_randr_add_modes_fixed() public API
xwayland: Make Xwayland rootful resizable
Xwayland: Do not mark decorate as experimental
xwayland: Use sensible defaults for rootful size
Revert "xwayland/glamor: Avoid implicit redirection with depth 32 parent windows"
xwayland: Move attach buffer out of post damage
xwayland: Use the screen width/height for libdecor state
xwayland: Move the libdecor resize to its own function
xwayland: attach new buffer from libdecor handlers
xwayland: Add configuration to libdecor update size
xwayland: Use update size from libdecor configure handler
xwayland: Set min/max size for rootful with lidecor
xwayland: Make fullscreen used a fixed size
xtest: Check whether there is a sendEventsProc to call
xwayland: Add an option to enable EI portal support
xwayland: Give up on EI on setup failure
xwayland: Cancel the EI disconnect timer when freed
xwayland: Add xwl_output to the Xwayland types
xwayland: Add a helper function to update fullscreen
xwayland: Update the fullscreen window on output change
xwayland: Do not resize when running fullscreen
build: Allow for custom server config directory
xwayland: Add an XACE property access handler
xwayland: Restrict allow commit to the window manager
xwayland: Avoid hardcoding the interface name
xwayland: Update output nameLength
xwayland: Use the right nameLength by default
xwayland: Pass the correct oeffis device types
build: Switch to meson 0.56
xwayland: Use a helper function for fullscreen update
xwayland: Use simpler initialization syntax
xwayland: Use the output serial for the fixed output
xwayland: Always create the XrandR CRTCs
xwayland: Do not update the outputs when rootful
xwayland: Add a function to search for xwl_output by name
xwayland: Add an output name for fullscreen
xwayland: Check for fullscreen on output name change
xwayland: Check for the screen output name for fullscreen
xwayland: Add the output name for fullscreen rootful
glx: Call XACE hooks on the GLX buffer
ephyr,xwayland: Use the proper private key for cursor
xwayland: Add a -nokeymap option
build: Use a variable for the xshmfence version
build: Xwayland with GLAMOR requires libxshmfence
xwayland: Move dmabuf code to its own source file
xwayland/glamor: Drop the EGLStream backend
xwayland/glamor: Add a GLAMOR GBM header
xwayland/glamor: Drop xwl_glamor_gbm_init_wl_registry()
xwayland/glamor: Drop xwl_glamor_gbm_has_wl_interfaces()
xwayland/glamor: Drop the init_egl() hook.
xwayland/glamor: Drop the init_screen() hook
xwayland/glamor: Drop the get_wl_buffer_for_pixmap() hook
xwayland/glamor: Drop the check_flip() hook
xwayland/glamor: Drop the get_main_device() hook
xwayland/glamor: Drop the create_pixmap_for_window() hook
xwayland/glamor: Drop the backend_flags
xwayland/glamor: Make xwl_glamor_init_gbm() return its status
xwayland/glamor: Remove the flag "is_available"
xwayland/glamor: Drop the post_damage() hook
xwayland/glamor: Drop the allow_commit() hook
xwayland/glamor: Make xwl_glamor_has_wl_interfaces() private
xwayland/glamor: Remove the backend pointers
xwayland/glamor: Drop init_backend() and select_backend()
xwayland/glamor: Remove the xwl_egl_backend structure
xwayland/glamor: Drop the backend_flags definition
xwayland/glamor: Drop xwl_screen_get_main_dev()
xwayland/glamor: Drop xwl_glamor_needs_buffer_flush()
xwayland/glamor: Drop xwl_glamor_needs_n_buffering()
xwayland: Drop xwl_window_buffers_get_pixmap()
xwayland: Add the Exec key to the desktop file
xwayland: Use full path for Xwayland exec
xwayland: Use "-decorate" if available
xwayland: Move the leave kbd/ptr code
xwayland: Introduce xwl_screen_lost_focus()
xwayland: Update lost focus on deactivation
xwayland: Use double for screen size
xwayland: Store the mode width/height
xwayland: Introduce output scale
xwayland: Use CRTC transforms
xwayland: Track output scales
xwayland: Add scale factor to the Xwayland screen
xwayland: Account for the scale factor
xwayland: Rename scale_x/y to viewport_scale_x/y
xwayland: Always set the viewport scale factor
xwayland: Apply the viewport's scale_x/y to all input
xwayland: Make has_viewport_enabled private
xwayland: Keep track of outputs per window
xwayland: Update the scale based on enter/leave events
xwayland: Update the global screen scale
xwayland: Rename xwl_window_enable_viewport()
build: Bump wayland-protocols requirement to 1.31
xwayland: Add support for fractional scale protocol
xwayland: Add helper function for fractional scaling
xwayland: Use fractional scale with rootful
render: Avoid possible double-free in ProcRenderAddGlyphs()
Revert "xwayland/glamor: Avoid implicit redirection with depth 32 parent windows"
xwayland: Walk the regions' boxes
xwayland: Use the path to Xwayland as installed
xwayland: Use exec name instead of hardcoding '/Xwayland'
xwayland: Define MAX_OUTPUT_NAME in the header
xwayland: Make xwl_output_set_name() public
xwayland: Check for duplicate output names
xwayland: Use the connector name for XRANDR leases
xwayland: Check for outputs before lease devices
xwayland: Do not remove output on withdraw if leased
xquartz: Remove invalid Unicode sequence
xwayland: Restore the ResizeWindow handler
xwayland: Handle rootful resize in ResizeWindow
xwayland: Move XRandR emulation to the ResizeWindow hook
xwayland: Do not use manual redirect windows as surface window
xwayland: Stop on first unmapped child
xwayland/window-buffers: Promote xwl_window_buffer
xwayland/window-buffers: Add xwl_window_buffer_release()
xwayland/glamor/gbm: Copy explicit sync code to GLAMOR/GBM
xwayland/window-buffers: Use synchronization from GLAMOR/GBM
xwayland/window-buffers: Do not always set syncpnts
xwayland/window-buffers: Move code to submit pixmaps
xwayland/window-buffers: Set syncpnts for all pixmaps
xwayland: Move xwl_window disposal to its own function
xwayland: Make sure we do not leak xwl_window on destroy
xwayland/window-buffers: Move buffer disposal to its own function
xwayland/window-buffers: optionally force disposal
xwayland: Force disposal of windows buffers for root on destroy
xwayland: Check for pointer in xwl_seat_leave_ptr()
xwayland: Make sure output is suitable for fullscreen
xwayland/ei: Handle EI_EVENT_KEYBOARD_MODIFIERS
xwayland/ei: Log the type name of unhandled events
glamor: Fix possible double-free
xwayland/ei: Move code to helper function
xwayland/ei: Dequeue events when all caps are available
xwayland: Fix build without DRI3 enabled
xwayland: Do not enable DRI3 without eventfd
xwayland: Do not include sys/eventfd.h without DRI3
xwayland: Report correct mode size when rootful
build: Move epoll dependency check
build: Add epoll to Xwayland for DragonFly and OpenBSD
build: Fix DRI3 on DragonFly and OpenBSD
os: Fix NULL pointer dereference
ci: Force build of default DDXen in the default target
ci: Check for DDXen to be built
ci: Install wayland-protocols 1.38
build: Bump wayland-protocols requirement to 1.38
xwayland: Add xdg-system-bell support
xwayland: Do not keep the cursor's pixmap around
xkb: Always use MAP_LENGTH keymap size
os/connection: Make sure partial is initialized
xwayland/glamor: Disable GLAMOR after GBM cleanup
Cursor: Refuse to free the root cursor
xkb: Fix buffer overflow in XkbVModMaskText()
xkb: Fix computation of XkbSizeKeySyms
xkb: Fix buffer overflow in XkbChangeTypesOfKey()
Xi: Fix barrier device search
composite: Handle failure to redirect in compRedirectWindow()
composite: initialize border clip even when pixmap alloc fails
dix: Dequeue pending events on frozen device on removal
sync: Do not let sync objects uninitialized
sync: Check values before applying changes
sync: Do not fail SyncAddTriggerToSyncObject()
sync: Apply changes last in SyncChangeAlarmAttributes()
test: Fix xsync test
xwayland: Do not pretend leaving the X11 surface if buttons are down
render: Avoid 0 or less animated cursors
os: Do not overflow the integer size with BigRequest
xfixes: Check request length for SetClientDisconnectMode
os: Account for bytes to ignore when sharing input buffer
record: Check for overflow in RecordSanityCheckRegisterClients()
randr: Check for overflow in RRChangeProviderProperty()
xfree86: Check for RandR provider functions
os: Check for integer overflow on BigRequest length
randr: Do not leak the provider property
present: Fix use-after-free in present_create_notifies()
xkb: Make the RT_XKBCLIENT resource private
xkb: Free the XKB resource when freeing XkbInterest
xkb: Prevent overflow in XkbSetCompatMap()
xwayland: Avoid premature surface commit running rootfull
xwayland: Expand tab characters
xwayland: Clean-up stray newlines
xwayland/ci: Enforce various code style checks
xwayland: Use viewport scale for warping coordinates
config: Fix compiler warning
xwayland: Commit surface on configure event
xkb: Fix bounds check in _CheckSetGeom()
miext/sync: Fix use-after-free in miSyncTriggerFence()
xkb: Fix out-of-bounds read in CheckModifierMap()
xkb: Add additional bound checking in CheckKeyTypes()
xkb: Add more _XkbCheckRequestBounds()
xwayland: Do not use pointer crossing count for slave devices
xwayland: Avoid NULL pointer dereference in damage_report()
dix: Add a selection bridge callback
dix: Add dixSetSelectionOwner()
xwayland: Add xwl_seat to the Xwayland types
xwayland: Add primary selection and data device protocols
xwayland: Implement clipboard and primary selection
xwayland: Add a new command line option to enable selection bridge
xwayland: Validate command line options separately
xwayland: Refuse to start with indirect GLX enabled
xwayland: Use output geometry by default when fullscreen
dix: Silent static analyzer warning
xkb: Fix potential uninitialized variable
config: Fix build with udev disabled
Revert "xwayland: Do not pretend leaving the X11 surface if buttons are down"
xwayland: Add have_clipboard flag in pkgconfig file
dix: Silence a compiler warning in doListFontsAndAliases()
dix: Silence a compiler warning in doListFontsWithInfo()
Xi: Check window attribute is valid in XIChangeCursor
test/pyxtest: fix ruff I001/UP035 import ordering
test/pyxtest: use int.bit_count() for virtual mods
test/pyxtest: use module logger instead of root logger
test/pyxtest: remove unnecessary pass in X11ConnectionError
test/pyxtest: annotate __enter__ return type as Self
test/pyxtest: catch OSError when closing Xlib display
test/pyxtest: create temp files with mkstemp
xwayland: Drop the seat from the list on destroy
xwayland: Drop expected events if the seat is destroyed
xwayland: Store the seat name
xwayland: Make xwl_screen_get_default_seat() public
xwayland: Use enable_device() for the pad
xwayland: Optionally disable devices on release
xwayland: Use Wayland seats for Xi2 devices
Patrick Lerda (1):
modesetting: find the first compatible dri device as default
Patrik Jakobsson (1):
modesetting: Fix dirty updates for sw rotation
Pavel Ondračka (2):
modesetting: byte-swap ARGB cursor uploads on big-endian
xwayland: let glamor initialize SHM fences
Pedro Montes Alcalde (1):
AutoRepeat: Fix wrong repeat rate being applied
Peter Grehan (1):
Fix build on FreeBSD/PowerPC architecture.
Peter Harris (3):
os: Restore buffer when writing to network
Update mailmap for Peter Harris
xkb: fix buffer re-use in _XkbSetCompatMap
Peter Hutterer (188):
xkb: fix XkbSetMap check for the keytypes count
xkb: move the SProcXkbDispatch declaration
xkb: rename xkb.h to xkb-procs.h
xkb: whitespace fixes
xkb: switch to array index loops to moving pointers
xkb: swap XkbSetDeviceInfo and XkbSetDeviceInfoCheck
xkb: add request length validation for XkbSetGeometry
xkb: fix some possible memleaks in XkbGetKbdByName
xkb: length-check XkbGetKbdByName before accessing the fields
xkb: length-check XkbListComponents before accessing the fields
xkb: proof GetCountedString against request length attacks
xwayland: correct the type for the discrete scroll events
xwayland: add support for the XWAYLAND extension
meson: add fontrootdir option to drop font-utils dependency
Xtest: disallow GenericEvents in XTestSwapFakeInput
Xi: disallow passive grabs with a detail > 255
Xext: free the XvRTVideoNotify when turning off from the same client
Xext: free the screen saver resource when replacing it
Xi: return an error from XI property changes if verification failed
Xi: avoid integer truncation in length check of ProcXIChangeProperty
xkb: reset the radio_groups pointer to NULL after freeing it
Xext: fix invalid event type mask in XTestSwapFakeInput
Fix some indentation issues
dix: remove unused PANORAMIX_DEBUG ifdef
dix: localize two variables
Disallow byte-swapped clients by default
xwayland: use a define for the horiz/vert scroll valuators
xwayland: hook up wl_pointer.axis_v120 events
Xi: fix potential use-after-free in DeepCopyPointerClasses
dix: remove pointless "flexible" x/y axis mapping
dix: switch scroll button emulation to multiples of increment
dix: fix wheel emulation lockup when a negative increment is set
xwayland: Add XTEST support using EIS
Xi/randr: fix handling of PropModeAppend/Prepend
mi: reset the PointerWindows reference on screen switch
dix: clean up the GestureInfoRec on device close
xkb: free the filters
randr: avoid integer truncation in length check of ProcRRChange*Property
Xi: allocate enough XkbActions for our buttons
Xi: require a pointer and keyboard device for XIAttachToMaster
dix: don't allow for devices with 0 axes
dix: use valuator_mask_free() to free the last touches vmask
test: fix various leaks in the tests
test: fix the xtest device test to show the dependency
test: fix the touch tests to no longer leak
dix: factor out the duplicate the RemoveDevice code paths
Two whitespace fixes
test: speed up the XISelectEvents test
meson.build: re-enable the protocol unit tests
test: drop the unncessary unit_defines from meson.build
xwayland: override the XTest sendEventsProc for all devices
dix: initialize the XTest sendEventsProc for all devices
Clean up the .gitignore file
dix: allocate enough space for logical button maps
dix: Allocate sufficient xEvents for our DeviceStateNotify
dix: fix DeviceStateNotify event calculation
Xi: when creating a new ButtonClass, set the number of buttons
Xi: flush hierarchy events after adding/removing master devices
dix: when disabling a master, float disabled slaved devices too
dix: fix valuator copy/paste error in the DeviceStateNotify event
test: switch the unit tests to something resembling a test suite
test: make wrapping a function more generic
test: switch the remaining wrapped functions to use the macros
test: specify non-negative log verbosity for the siglogging test
test: use a dbg() macro for the test output
CI: use MESON_BUILDDIR for the build directory
CI: switch to the meson-build.sh helper script
CI: switch the mingw cross-compile job to use the meson build script too
CI: replace the dist script with invocations of the meson-build script
CI: add a driver build stage to check for header breakage
CI: Only run the driver build job on Xorg changes
render: fix refcounting of glyphs during ProcRenderAddGlyphs
test: fix the xi2 protocol swapping tests to actually work
CI: include ci-templates only once
dix: don't push the XKB state to a non-existing master keyboard
Xi: when removing a master search for a disabled paired device
Ignore the coding style change commit during git blame
dix: keep a ref to the rootCursor
mi: don't crash on miPointerGetPosition for disabled devices
mi: guard miPointer functions against NULL dereferences
Xi: disallow grabbing disabled devices
dix: fix erroneous BUG_RETURN check
meson.build: print a summary of the DDX to build
dix: pick the right keyboard for focus FollowKeyboard
CI: drop the ci-fairy check-mr job
damageext: fix wrong REQUEST_SIZE_MATCH type in SProcDamageAdd
randr: fix wrong size check and missing swaps in SProcRRSetMonitor
Zero out structs to avoid leaking information via padding
Xext/xres: add missing byte-swap of spec entries in SProcXResQueryClientIds
Xext/xres: fix wrong swap check
Xext/xres: fix undefined behavior in ConstructClientIdValue
Xext/shm: add missing reply byte-swap in ProcShmCreateSegment
Xi: add missing byte-swap of resolution values in SProcXChangeDeviceControl
render: add missing byte-swap of filter params in SProcRenderSetPictureFilter
glx: fix wrong pointer passed to non-swap handlers in TexImage/CopySubBuffer
glx/glxcmdsswap: add missing contextTag byte-swap in __glXDispSwap_CopyContext
randr, Xext: remove stale length swaps
Xext/vidmode: fix SProcVidModeSwitchToMode swapping only screen field
randr: add missing byte swapping for various fields
present: add missing byte swapping for various fields
pseudoramiX: add missing byte swapping in various fields
Xext/vidmode: add byte-swapping in various fields
Xext/sync: add a missing byte swap
meson.build: fix erroneous path expansion
os/access: handle strdup failure in ComputeLocalClient
os/client: fix kvm handle leak and NULL dereferences on OpenBSD
dix: handle various allocation failures
Xext: handle various allocation failures
panoramiX: fail if we can't allocate our visual arrays
Xi: add NULL checks to handle malloc failures
Xi: fail if we can't assign device names
glx: fail if we can't init a screen
glx: handle strdup allocation failures
mi: fail on reallocarray failure in miAppendSpans
mi: Handle allocation failure in XYToWindow() spriteTrace realloc
hw/xwayland: handle wl_array_add failure in keyboard_handle_key
hw/xwayland: fix missing NULL checks in DRM lease allocation paths
modesetting: add NULL check for drmModeObjectGetProperties in VRR check
xkb: add missing NULL check for strdup in XkbAddGeomProperty update path
xkb: fix client-triggerable memory leak in ProcXkbGetKbdByName
xkb: fail if we can't strdup our default rules
xkb: Handle allocation failures in _XkbNextFreeFilter()
Xi: Fix XIPassiveGrab handling of keycodes > 255
Xi: fix ProcXIGrabDevice returning AlreadyGrabbed as X error code
Xi: Swap property data in SProcXChangeDeviceProperty/SProcXIChangeProperty
present: Fix missing byte swaps in sproc_present_pixmap()
modesetting: Fix double increment in cursor buffer cleanup loop
Xi: add missing gesture grab type checks in ProcXIPassiveUngrabDevice
xkb: Fix out-of-bounds array access in _CheckSetShapes()
xkb: Fix off-by-one in color index validation in _CheckSetGeom()
xkb: Fix off-by-one and NULL dereferences in _CheckSetOverlay()
xkb: Add bounds check for action data in CheckKeyActions()
xkb: Fix out-of-bounds array access in xkmread.c ReadXkmGeometry
os/auth: fix error paths when reading from /dev/urandom
os/log: handle NULL string argument in vpnprintf
os/access: fix off-by-one in hostname character validation range
Xext/xres: fix client PID value swap in ConstructClientIdValue
Xi/xichangehierarchy: reject zero-length hierarchy change entries
Xi/exevents: fix off-by-one in UpdateDeviceState valuator bounds check
randr/rrsdispatch: reject invalid format in SProcRRChangeProviderProperty
os/auth: prefer getrandom() over arc4random_buf() and /dev/urandom
render: fix memory leaks on XaceHook failure in resource creation
present: actually return the created notifies
meson: give the xorg executable an actual name
test: add pytest-based test suite
pyxtest: add tests for XI property and passive grab CVEs
pyxtest: add test cases for the RandR extension CVEs of the last years
pyxtest: add test cases for the various XKB CVEs from the last few years
byxtest: add test cases for the RECORD extension CVEs of the last years
pyxtest: add test cases for the Screensaver extension CVEs of the last years
pyxtest: add tests for the byteswapping patches
pyxtest: add tests for XI property data byte-swap fix
pyxtest: add --display for running a test against a manually started server
pyxtest: add test cases for the recent XKB fixes
pyxtest: add test for present notify array byte-swap fix
pyxtest: fix xorg invocations when running from the build dir
pyxtest: require root to run the test as Xorg
pyxtest: fix the vidmode SwitchToModeRequest test
cursor: fix AllocARGBCursor leak/double-free for psrcbits/pmaskbits/argb
dix/colormap: fix out-of-bounds read in FindColorInRootCmap
glx: reject negative size in FeedbackBuffer and SelectBuffer requests
pyxtest: document the --display option in the README
pyxtest: replace numerical error values with BadValue, etc.
pyxtest: rework the request handling to avoid to_bytes() invocations
sync: fix deletion of counters and fences
sync: restart trigger list iteration in SyncChangeCounter after TriggerFired
xkb: reject key types with num_levels exceeding XkbMaxShiftLevel
xkb: clamp nMaps to mapWidths buffer size in CheckKeyTypes
glx: fix reversed length check in ChangeDrawableAttributes
saver: re-fetch screen private after CheckScreenPrivate in CreateSaverWindow
dix: increase XLFDMAXFONTNAMELEN to match libXfont2's MAXFONTNAMELEN
test/pyxtest: add test for GLX ChangeDrawableAttributes OOB read (ZDI-CAN-30165)
test/pyxtest: add tests for miSyncDestroyFence/FreeCounter (ZDI-CAN-30159/30163)
test/pyxtest: add test for SyncChangeCounter trigger list UAF (ZDI-CAN-30164)
test/pyxtest: add test for ScreenSaver CreateSaverWindow UAF (ZDI-CAN-30168)
test/pyxtest: add test for XKB num_levels stack overflow (ZDI-CAN-30160)
test/pyxtest: add test for XKB mapWidths stack OOB write (ZDI-CAN-30161)
test/pyxtest: add test for font alias stack overflow (ZDI-CAN-30136)
test/pyxtest: add test for ScreenSaverFreeAttr stale pPriv code path
glx: fix duplicate tagInfo->vendor = NULL assignment
glamor: fix an error path cleanup
glx: free old context tag before allocating new one in CommonMakeCurrent
fb/mi/glamor: reject glyphs with negative dimensions
glamor: reject fonts with per-glyph metrics exceeding maxbounds
test/pyxtest: allow for extra arguments in the xserver fixture
test/pyxtest: move X11 error codes from xclient.py to proto/x11.py
Disable font server connections by default
test/pyxtest: add PictFormInfo and QueryPictFormatsReply to render proto
Pierre Le Marre (2):
xkb: Fix key type without level names in XkbCopyKeymap
xkb: Fix serialization of key type without level names
Pierre-Eric Pelloux-Prayer (5):
glamor: return the result of gbm_format_for_depth
glamor: use gbm_format_for_depth instead of open-coding it
glamor: reject configs using unsupported rgbBits size
modesetting: use gbm_bo_create_with_modifiers2 when possible
modesetting: use GBM_BO_USE_FRONT_RENDERING for front_bo
Povilas Kanapickas (25):
meson: Add option to disable libdrm support
meson: Implement developer documentation build
Drop DMX DDX
glamor: Fix handling of 1-bit pixmaps
Remove autotools support
meson: Bump version after X server 21.1 branch off
Revert "hw/xfree86: Propagate physical dimensions from DRM connector"
meson: Correctly set DDXOSVERRORF and DDXBEFORERESET on xwin
xwayland: Implement support for touchpad gestures
xwayland: Fix a race condition when setting up input devices
record: Fix out of bounds access in SwapCreateRegister()
xfixes: Fix out of bounds access in *ProcXFixesCreatePointerBarrier()
Xext: Fix out of bounds access in SProcScreenSaverSuspend()
render: Fix out of bounds access in SProcRenderCompositeGlyphs()
Remove *-config.h.in which were only used by autotools
meson: Remove config macros that are no longer used
dix: Correctly save replayed event into GrabInfoRec
dix: Fix use after free in input device shutdown
dix: Don't send touch end to clients that do async grab without touches
xfree86: Fix event data alignment in inputtest driver
ci: Point to last commit of xf86-video-qxl instead of master branch
ci: Adjust prefix instead of setting DESTDIR for meson-dist job
ci: Add install prefix to the artifacts of meson-dist job
ci: Reuse xserver created by meson-dist job in driver build jobs
Revert "glamor: explicitly draw endpoints of line segments"
Qiang Yu (2):
modesetting: fix PRESENT_FLIP_REASON_BUFFER_FORMAT gets overwritten
glamor: enable dmabuf_capable by default for radeonsi
Randy Palamar (1):
os/osinit: fix build when execinfo.h is missing
Ray Strode (1):
xkb: Drop check for XkbSetMapResizeTypes
Richard Purdie (1):
COPYING: Add SPDX-License-Identifier entries
Roman Gilg (1):
Remove build-only include from public header
Rouven Czerwinski (2):
xwayland: remove includedir from pkgconfig
xwayland: install pkgconfig to sharedir
Russell Chou (1):
xwayland: Clean up drm lease when terminating. #946
Sam James (3):
hw/xfree86: fix sbus build for SPARC
Switch to libbsd-overlay
meson: add option for systemd_notify
Samuel Thibault (1):
xkb: fix XkbSetMap when changing a keysym without changing a keytype
Shashank Sharma (1):
xf86: allow DDX driver for GPU/PCI hot-plug
Simon Ser (18):
xwayland: fix xdg_output leak
xwayland: add -noTouchPointerEmulation
xwayland: fix -noTouchPointerEmulation
meson: use add_project_arguments instead of add_global_arguments
meson: add subproject fallback for libxcvt
xwayland: fix GBM on driver without explicit modifiers
xwayland: generate pkg-config file from Meson
xwayland: override Meson dependency
xwayland: fix error path when modifier is not supported
xwayland: don't fall back to wl_drm with explicit modifier
xwayland: use drmDevice to compare DRM devices
Allow disabling the SHAPE extension at runtime
xwayland: use gbm_bo_create_with_modifiers2()
build: set _GNU_SOURCE when checking for SO_PEERCRED
xwayland/glamor/gbm: use Bool for true/false fields
xwayland/glamor/gbm: make wl_drm optional
xwayland/glamor/gbm: simplify render node check
xwayland: use array for protocol XML files
Spiky Caterpillar (1):
No longer leak FDs on VT switch.
Sultan Alsawaf (20):
pixmap: make PixmapDirtyCopyArea public
xfree86: make xf86RotateCrtcRedisplay public
modesetting: make the shadow buffer helpers generic
modesetting: make do_queue_flip_on_crtc generic
present: add awareness for drivers with TearFree
modesetting: coalesce vblank events to avoid DRM event queue exhaustion
modesetting: add support for TearFree page flips
modesetting: Remove redundant GLAMOR_HAS_GBM #ifdef from ms_do_pageflip
modesetting: Pass reference CRTC pointer to ms_do_pageflip
modesetting: Pass CRTC pointer to TearFree flip handlers
modesetting: Fix memory leak on ms_do_pageflip error
modesetting: Improve TearFree state check in ms_present_check_flip
modesetting: Introduce ms_tearfree_is_active_on_crtc helper
modesetting: Ensure vblank events always run in sequential order
modesetting: Support accurate DRI presentation timing with TearFree
present: Prevent double vblank enqueue on error when TearFree is used
present: Fix inaccurate PresentCompleteNotify timing for TearFree
present: Document the TearFree flip reasons in PresentFlipReason
modesetting: Enable TearFree by default
modesetting: Don't recursively force present to unflip
Sérgio Basto (1):
Revert "fb: Declare wfbFinishScreenInit, wfbScreenInit for !FB_ACCESS_WRAPPER"
Takashi Yano (1):
Fix mach64 driver crash
Tamura Dai (2):
Xephyr: fix help output.
Xephyr: fix tiny memleak in KdParseKeyboard().
Tanguy Ortolo (1):
xorg.conf.man: Complete the xorg.conf.5 manpage with Option "Disable"
Thomas Zimmermann (5):
xf86: Accept devices with the 'hyperv_drm' driver
xf86: Accept devices with the kernel's ofdrm driver
xf86: Accept devices with the kernel's efidrm driver
xf86: Accept devices with the kernel's vesadrm driver
xf86: Accept devices with the kernel's corebootdrm driver
Timo Aaltonen (1):
xf86pciBus.c: use Intel ddx only for pre-gen3 hardware
Tj (1):
xfree86: fbdevhw: fix pci detection on recent Linux
Tom Yan (2):
xnest/mi: remove redundant call of miScreenDevPrivateInit()
mi: decouple miCreateScreenResources from pScreen->{width,height}
Trevor Davenport (1):
modesetting: Fix invalid identity CTM on 32-bit.
Twaik Yont (2):
xvfb: Use RROutputSetPhysicalSize to set physical size of display
os: use close-on-exec for X server socket to prevent fd leaks
Vasily Khoruzhick (1):
glamor: use dual source blend on GL 2.1 with ARB_ES2_compatibility
Ville Syrjälä (4):
modesetting: unflip before any setcrtc() calls
modesetting: Use a more optimal hw cursor size
modesetting: Don't feed stack garbage to the kernel in LUT reserved fields
glamor: Enable dmabuf_capable by default on Intel hardware
Vlad Zahorodnii (6):
xwayland: Set wl_surface input region
xwayland: Use correct xwl_window lookup function in xwl_set_shape
xwayland: Dispatch tablet tool tip events after frame events
ci: Bump wayland to 1.26
xwayland: Add support for wl_fixes.destroy_global
xwayland: Add support for wl_fixes.ack_global_remove
Wanli Niu (1):
dix: Fix segfault if CreateGC() failed in XaceHook()
Warren Togami (1):
xwayland: Ensure pointer for gestures has buttons
Weng Xuetian (1):
xwayland: Fix invalid pointer access in drm_lease_device_handle_released.
Willem Jan Palenstijn (1):
mi: fix rounding issues around zero in miPointerSetPosition
Xaver Hugl (9):
Update the CI to provide wayland-protocols 1.22
require wayland-protocols 1.22
randr: add new interface to allow delaying lease responses
Update the CI to provide wayland-protocols 1.30
require wayland-protocols 1.30
Update CI to xorgproto 2023.2
present: add support for PresentOptionAsyncMayTear
xwayland: add support for wp-tearing-control-v1
xwayland: add workaround for drivers that don't support impicit sync
Xinhao Liu (1):
composite: Fix PanoramiX overlay window release
Yao Wei (1):
dix: Force update LEDs after device state update in EnableDevice
YaoBing Xiao (1):
xwayland: prevent potential null pointer dereference
Yixue Wang (1):
xwayland: wrong expecting_event
Yuriy Vasilev (3):
glamor: fix CbCr format handling
glamor: xv: add rgba32 format
glamor: xv: add rgb565
Yusuf Khan (2):
hw/xfree86: fix NULL pointer refrence to mode name
modesetting/dri2: Remove always true ifdef
Zoltán Böszörményi (4):
xf86: Extract screen configuration matching into its own function
xf86: Assign GPUs to screens according to configuration
glamoregl: Initialize glamor on the main device
Use log lines prefixed with human readable time
dongshengyuan (1):
enhance: popen-fdopen-error-handling
hongao (1):
randr: clear primary screen's primaryOutput when the output is deleted
liuheng (1):
config: Preserve section data when parsing duplicate files
matt335672 (1):
Add docs for some internal methods
moozcheng (1):
dix: fix a misused const pointer in cursor.c
msizanoen1 (1):
glamor: Use render node for glamor device path where possible
nerdopolis (5):
xf86: Accept devices with the 'simpledrm' driver.
os: Try to discover the current seat with the XDG_SEAT var first
xfree86: On Linux, while only seat0 can have TTYs, don't assmume all seat0s have TTYs
xephyr: Don't check for SeatId anymore
modesetting: Fix hang when all probed cursor sizes fail to find a minimum one
nia (2):
config/wscons: Fix build and add support for NetBSD
config/wscons: Always attach the "ws" driver for pointer devices,
orbea (1):
meson: wayland_client_dep is false when wayland is disabled
pkubaj (1):
Fix build on FreeBSD/powerpc*
quantenzitrone (2):
COPYING: add missing paragraph to SGI-B-2.0
COPYING: add author to HPND-sell-MIT-disclaimer-xserver
stefan11111 (5):
composite: Only copy bits from the parent pixmap when absolutely necessary
glamor: fix Option "GlxVendorLibrary"
kdrive: Don't fixup the cursor position twice in KdCursorOffScreen
randr: Set the legacy RandR size range to include rotations
kdrive/ephyr: Fix typo when checking for `EGL_KHR_platform_x11`
tholin (1):
dix: Hold input lock for AttachDevice()
xurui (2):
modesetting: Check the return value of the drmGetVersion
xwayland: Use do-while loop
zhoulei (1):
xwayland: Change randr_output status when call xwl_output_remove()
Łukasz Spintzyk (2):
present: fallback get_crtc to return crtc belonging to screen with present extension
modesetting: unflip not possible when glamor is not set
--
-Alan Coopersmith- alan.coopersmith at oracle.com
Oracle Solaris Engineering - https://blogs.oracle.com/solaris
-------------- next part --------------
A non-text attachment was scrubbed...
Name: signature.asc
Type: application/pgp-signature
Size: 870 bytes
Desc: not available
URL: <https://lists.x.org/archives/xorg-announce/attachments/20260819/9bbf792c/attachment-0001.sig>



More information about the xorg-announce
mailing list