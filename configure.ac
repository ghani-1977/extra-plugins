AC_INIT([enigma2-alliance-plugins],[1.0])
AM_INIT_AUTOMAKE([dist-bzip2 foreign no-define tar-pax])
AC_CONFIG_HEADERS([enigma2-plugins-config.h])

# Silent rules are available since 1.11, but older versions
# are still in use. So don't use them unconditionally.
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

AC_USE_SYSTEM_EXTENSIONS
AC_SYS_LARGEFILE

AC_PROG_CC
AC_PROG_CXX
m4_ifdef([LT_INIT], [LT_INIT], [AC_PROG_LIBTOOL])
AC_CONFIG_MACRO_DIR([m4])

AC_CHECK_HEADERS([dbox/fp.h dbox/lcd-ks0713.h])

AC_PATH_PROG(MSGFMT, msgfmt, AC_MSG_ERROR(Could not find msgfmt))
AC_PATH_PROG(MSGINIT, msginit, AC_MSG_ERROR(Could not find msginit))
AC_PATH_PROG(MSGMERGE, msgmerge, AC_MSG_ERROR(Could not find msgmerge))
AC_PATH_PROG(MSGUNIQ, msguniq, AC_MSG_ERROR(Could not find msguniq))
AC_PATH_PROG(XGETTEXT, xgettext, AC_MSG_ERROR(Could not find xgettext))

AM_PATH_PYTHON
AX_PYTHON_DEVEL
AX_PTHREAD

AC_ARG_WITH(amlplugins,
	AC_HELP_STRING([--with-amlplugins], [have amlplugins]),
	[[withamlplugins=$withval]],
	[[withamlplugins=no]]
)
if test x"$withamlplugins" != xno ; then
	AC_DEFINE(HAVE_AMLPLUGINS, 1,[Define when using a amlplugins])
fi
AM_CONDITIONAL(HAVE_AMLPLUGINS, test x"$withamlplugins" != xno)


AC_ARG_WITH(arch,
	[  --with-arch=NAME box arch [[none,ah4,mipsel...]]],
	[ARCH="$withval"],[ARCH="mipsel"])
AC_SUBST(ARCH)
AC_DEFINE_UNQUOTED(ARCH,"$ARCH",[box arch])

AM_CONDITIONAL(SH4, test `echo "$ARCH" | cut -b 1-3` == "sh4")
AM_CONDITIONAL(MIPSEL, test `echo "$ARCH" | cut -b 1-6` == "mipsel")
AM_CONDITIONAL(ARM, test `echo "$ARCH" | cut -b 1-3` == "arm")

AC_ARG_WITH(boxtype,
	[  --with-boxtype=NAME box type [[none,dm800...]]],
	[BOXTYPE="$withval"],[BOXTYPE="dm800"])
AC_SUBST(BOXTYPE)
AC_DEFINE_UNQUOTED(BOXTYPE,"$BOXTYPE",[box type])

AM_CONDITIONAL(DREAMBOX, test `echo "$BOXTYPE" | cut -b 1-2` == "dm")
AM_CONDITIONAL(XTREND, test `echo "$BOXTYPE" | cut -b 1-2` == "et")
AM_CONDITIONAL(INI, test `echo "$BOXTYPE" | cut -b 1-3` == "ini")
AM_CONDITIONAL(GIGABLUE, test `echo "$BOXTYPE" | cut -b 1-2` == "gb")
AM_CONDITIONAL(ODIN, test `echo "$BOXTYPE" | cut -b 1-4` == "odin")

AM_CONDITIONAL(HD2400, test "$BOXTYPE" == "hd2400")
AM_CONDITIONAL(HD1500, test "$BOXTYPE" == "hd1500")
AM_CONDITIONAL(HD1265, test "$BOXTYPE" == "hd1265")
AM_CONDITIONAL(HD1200, test "$BOXTYPE" == "hd1200")
AM_CONDITIONAL(HD1100, test "$BOXTYPE" == "hd1100")
AM_CONDITIONAL(HD500C, test "$BOXTYPE" == "hd500c")
AM_CONDITIONAL(HD530C, test "$BOXTYPE" == "hd530c")
AM_CONDITIONAL(OSMIO4K, test "$BOXTYPE" == "osmio4k")
AM_CONDITIONAL(VUUNO, test "$BOXTYPE" == "vuuno")
AM_CONDITIONAL(VUULTIMO, test "$BOXTYPE" == "vuultimo")
AM_CONDITIONAL(VUSOLOSE, test "$BOXTYPE" == "vusolose")
AM_CONDITIONAL(VUDUO, test "$BOXTYPE" == "vuduo")
AM_CONDITIONAL(VUSOLO2, test "$BOXTYPE" == "vusolo2")
AM_CONDITIONAL(VUSOLO4K, test "$BOXTYPE" == "vusolo4k")
AM_CONDITIONAL(VUUNO4K, test "$BOXTYPE" == "vuuno4k")
AM_CONDITIONAL(VUUNO4KSE, test "$BOXTYPE" == "vuuno4kse")
AM_CONDITIONAL(VUULTIMO4K, test "$BOXTYPE" == "vuultimo4k")
AM_CONDITIONAL(VUZERO4K, test "$BOXTYPE" == "vuzero4k")
AM_CONDITIONAL(VUDUO2, test "$BOXTYPE" == "vuduo2")
AM_CONDITIONAL(VUDUO4K, test "$BOXTYPE" == "vuduo4k")
AM_CONDITIONAL(VUZERO, test "$BOXTYPE" == "vuzero")
AM_CONDITIONAL(XP1000, test "$BOXTYPE" == "xp1000")
AM_CONDITIONAL(VS1000, test "$BOXTYPE" == "vs1000")

if test `echo "$BOXTYPE" | cut -b 1-2` == "dm"; then
	AC_DEFINE(DREAMBOX, 1, [Dreambox hardware])
fi

AM_CONDITIONAL(HAVE_MICOM, test "$BOXTYPE" == "atemio5x00" -o "$BOXTYPE" == "atemio6000" -o "$BOXTYPE" == "atemio6100" -o "$BOXTYPE" == "atemio6200" -o "$BOXTYPE" == "atemionemesis" -o "$BOXTYPE" == "beyonwizt2" -o "$BOXTYPE" == "beyonwizt3" -o "$BOXTYPE" == "beyonwizt4" -o "$BOXTYPE" == "bwidowx" -o "$BOXTYPE" == "bwidowx2" -o "$BOXTYPE" == "evoslim" -o "$BOXTYPE" == "mbhybrid" -o "$BOXTYPE" == "mbmini" -o "$BOXTYPE" == "mbminiplus" -o "$BOXTYPE" == "mbtwin" -o "$BOXTYPE" == "mbultra" -o "$BOXTYPE" == "opticumtt" -o "$BOXTYPE" == "sezam1000hd" -o "$BOXTYPE" == "sezam5000hd" -o "$BOXTYPE" == "sezammarvel" -o "$BOXTYPE" == "ventonhdx" -o "$BOXTYPE" == "xpeedlx" -o "$BOXTYPE" == "xpeedlx3")
AM_CONDITIONAL(HAVE_ARMV7A, test "$BOXTYPE" == cube)
AM_CONDITIONAL(HAVE_ARMV7AHF, test "$BOXTYPE" == "hd51" -o "$BOXTYPE" == "8100s" -o "$BOXTYPE" == "vs1500" -o "$BOXTYPE" == "vusolo4k" -o "$BOXTYPE" == "vuuno4k" -o "$BOXTYPE" == "vuuno4kse" -o "$BOXTYPE" == "vuzero4k" -o "$BOXTYPE" == "vuultimo4k" -o "$BOXTYPE" == "vuduo4k" -o "$BOXTYPE" == "dm900" -o "$BOXTYPE" == "dm920" -o "$BOXTYPE" == "sf4008" -o "$BOXTYPE" == "dags7252" -o "$BOXTYPE" == "dags72604" -o "$BOXTYPE" == "gb7252" -o "$BOXTYPE" == "xc7439" -o "$BOXTYPE" == "h7" -o "$BOXTYPE" == "h9" -o "$BOXTYPE" == "h9combo" -o "$BOXTYPE" == "sf5008" -o "$BOXTYPE" == "et1x000" -o "$BOXTYPE" == "et13000" -o "$BOXTYPE" == "cc1" -o "$BOXTYPE" == "sf8008" -o "$BOXTYPE" == "hd60" -o "$BOXTYPE" == "hd61" -o "$BOXTYPE" == "i55plus" -o "$BOXTYPE" == "ustym4kpro" -o "$BOXTYPE" == "v8plus" -o "$BOXTYPE" == "multibox")
AM_CONDITIONAL(HAVE_CORTEXA9HF, test "$BOXTYPE" == "wetekplay")
AM_CONDITIONAL(HAVE_AARCH64, test "$BOXTYPE" == "wetekplay2" -o "$BOXTYPE" == "alien5" -o "$BOXTYPE" == "osmio4k")

AC_CONFIG_FILES([
Makefile

AudioEffect/Makefile
AudioEffect/src/Makefile
AudioEffect/meta/Makefile
AudioEffect/po/Makefile

AnimationSetup/Makefile
AnimationSetup/src/Makefile
AnimationSetup/po/Makefile
AnimationSetup/meta/Makefile

Blindscan/Makefile
Blindscan/src/Makefile
Blindscan/meta/Makefile
Blindscan/po/Makefile

ChannelsImporter/Makefile
ChannelsImporter/meta/Makefile
ChannelsImporter/po/Makefile
ChannelsImporter/src/Makefile

DLNABrowser/Makefile
DLNABrowser/src/Makefile
DLNABrowser/icons/Makefile
DLNABrowser/po/Makefile
DLNABrowser/meta/Makefile

DLNAServer/Makefile
DLNAServer/src/Makefile
DLNAServer/po/Makefile
DLNAServer/meta/Makefile

DMBlindscan/Makefile
DMBlindscan/src/Makefile
DMBlindscan/meta/Makefile
DMBlindscan/po/Makefile

ABMCustomMixImporter/Makefile
ABMCustomMixImporter/meta/Makefile
ABMCustomMixImporter/po/Makefile
ABMCustomMixImporter/src/Makefile
ABMCustomMixImporter/mixes/Makefile

FirmwareUpgrade/Makefile
FirmwareUpgrade/src/Makefile
FirmwareUpgrade/meta/Makefile
FirmwareUpgrade/po/Makefile

Fempa/Makefile
Fempa/meta/Makefile
Fempa/src/Makefile
Fempa/po/Makefile

FPGAUpgrade/Makefile
FPGAUpgrade/src/Makefile
FPGAUpgrade/meta/Makefile
FPGAUpgrade/po/Makefile

GigaBlueRemote/Makefile
GigaBlueRemote/src/Makefile
GigaBlueRemote/meta/Makefile
GigaBlueRemote/po/Makefile

GigaBlueVFDControl/Makefile
GigaBlueVFDControl/src/Makefile
GigaBlueVFDControl/meta/Makefile
GigaBlueVFDControl/po/Makefile

INIVFDControl/Makefile
INIVFDControl/src/Makefile
INIVFDControl/meta/Makefile
INIVFDControl/po/Makefile

EWVFDControl/Makefile
EWVFDControl/src/Makefile
EWVFDControl/meta/Makefile
EWVFDControl/po/Makefile

F3LEDControl/Makefile
F3LEDControl/src/Makefile
F3LEDControl/meta/Makefile
F3LEDControl/po/Makefile

VPLEDControl/Makefile
VPLEDControl/src/Makefile
VPLEDControl/meta/Makefile
VPLEDControl/po/Makefile

OdinM7VFDControl/Makefile
OdinM7VFDControl/src/Makefile
OdinM7VFDControl/meta/Makefile
OdinM7VFDControl/po/Makefile

MICOMUpgrade/Makefile
MICOMUpgrade/src/Makefile
MICOMUpgrade/src/bin/Makefile
MICOMUpgrade/meta/Makefile
MICOMUpgrade/po/Makefile
MICOMUpgrade/buttons/Makefile

MultiTransCodingSetup/Makefile
MultiTransCodingSetup/src/Makefile
MultiTransCodingSetup/meta/Makefile
MultiTransCodingSetup/po/Makefile

OnDemand/Makefile
OnDemand/src/Makefile
OnDemand/src/icons/Makefile
OnDemand/meta/Makefile
OnDemand/po/Makefile

TempFanControl/Makefile
TempFanControl/src/Makefile
TempFanControl/meta/Makefile
TempFanControl/po/Makefile

TerrestrialScan/Makefile
TerrestrialScan/images/Makefile
TerrestrialScan/lib/Makefile
TerrestrialScan/meta/Makefile
TerrestrialScan/po/Makefile
TerrestrialScan/src/Makefile

TunerServer/Makefile
TunerServer/src/Makefile
TunerServer/meta/Makefile
TunerServer/po/Makefile

ReZap/Makefile
ReZap/src/Makefile
ReZap/meta/Makefile

RCUSelect/Makefile
RCUSelect/src/Makefile
RCUSelect/conf/Makefile
RCUSelect/po/Makefile
RCUSelect/meta/Makefile

SatipClient/Makefile
SatipClient/src/Makefile
SatipClient/po/Makefile
SatipClient/meta/Makefile

SimpleFancontrol/Makefile
SimpleFancontrol/src/Makefile
SimpleFancontrol/meta/Makefile
SimpleFancontrol/po/Makefile

SF8VFDControl/Makefile
SF8VFDControl/src/Makefile
SF8VFDControl/meta/Makefile
SF8VFDControl/po/Makefile

StreamTV/Makefile
StreamTV/src/Makefile
StreamTV/meta/Makefile
StreamTV/po/Makefile
StreamTV/icons/Makefile

VentonFancontrol/Makefile
VentonFancontrol/src/Makefile
VentonFancontrol/meta/Makefile
VentonFancontrol/po/Makefile

VuRemote/Makefile
VuRemote/src/Makefile
VuRemote/meta/Makefile
VuRemote/po/Makefile

VuDuoFanControl/Makefile
VuDuoFanControl/src/Makefile
VuDuoFanControl/meta/Makefile
VuDuoFanControl/po/Makefile

WebBrowser/Makefile
WebBrowser/src/Makefile
WebBrowser/meta/Makefile
WebBrowser/keymap/Makefile
WebBrowser/icons/Makefile
WebBrowser/po/Makefile

WirelessAccessPoint/Makefile
WirelessAccessPoint/src/Makefile
WirelessAccessPoint/meta/Makefile
WirelessAccessPoint/po/Makefile

xmlUpdate/Makefile
xmlUpdate/meta/Makefile
xmlUpdate/po/Makefile
xmlUpdate/src/Makefile

XtrendFancontrol/Makefile
XtrendFancontrol/src/Makefile
XtrendFancontrol/meta/Makefile
XtrendFancontrol/po/Makefile

XtrendRemote/Makefile
XtrendRemote/src/Makefile
XtrendRemote/meta/Makefile
XtrendRemote/po/Makefile

])
AC_OUTPUT
