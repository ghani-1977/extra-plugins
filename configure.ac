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

AC_ARG_WITH(boxbrand,
	[  --with-boxbrand=NAME box brand [[none,dreambox...]]],
	[BOXBRAND="$withval"],[BOXBRAND="dreambox"])
AC_SUBST(BOXBRAND)
AC_DEFINE_UNQUOTED(BOXBRAND,"$BOXBRAND",[box brand])

AM_CONDITIONAL(DINOBOT, test "$BOXTYPE" == "anadol4k" -o "$BOXTYPE" == "anadol4kv2" -o "$BOXTYPE" == "axashis4kcombo" -o "$BOXTYPE" == "axashis4kcomboplus" -o "$BOXTYPE" == "dinobot4k" -o "$BOXTYPE" == "dinobot4kl" -o "$BOXTYPE" == "dinobot4kmini" -o "$BOXTYPE" == "dinobot4kplus" -o "$BOXTYPE" == "dinobot4kpro" -o "$BOXTYPE" == "dinobot4kse" -o "$BOXTYPE" == "axashisc4k" -o "$BOXTYPE" == "dinobotu43" -o "$BOXTYPE" == "dinobotu55" -o "$BOXTYPE" == "protek4kx1" -o "$BOXTYPE" == "spycatminiv2" -o "$BOXTYPE" == "iziboxecohd" -o "$BOXTYPE" == "iziboxx3" -o "$BOXTYPE" == "jdhdduo" -o "$BOXTYPE" == "turing" -o "$BOXTYPE" == "arivatwin" -o "$BOXTYPE" == "arivacombo")

AM_CONDITIONAL(HAVE_ARMV7A, test "$BOXTYPE" == "cube" -o "$BOXTYPE" == "su980")

AM_CONDITIONAL(HAVE_ARMV7AHF, test "$BOXTYPE" == "hd51" -o "$BOXTYPE" == "e4hdultra" -o "$BOXTYPE" == "protek4k" -o "$BOXTYPE" == "vs1500" -o "$BOXTYPE" == "vusolo4k" -o "$BOXTYPE" == "vuuno4k" -o "$BOXTYPE" == "vuuno4kse" -o "$BOXTYPE" == "vuzero4k" -o "$BOXTYPE" == "vuultimo4k" -o "$BOXTYPE" == "vuduo4k" -o "$BOXTYPE" == "dm900" -o "$BOXTYPE" == "dm920" -o "$BOXTYPE" == "sf4008" -o "$BOXTYPE" == "force3uhdplus" -o "$BOXTYPE" == "force3uhd" -o "$BOXTYPE" == "revo4k" -o "$BOXTYPE" == "tmtwin4k" -o "$BOXTYPE" == "galaxy4k" -o "$BOXTYPE" == "tm4ksuper" -o "$BOXTYPE" == "lunix34k" -o "$BOXTYPE" == "force4" -o "$BOXTYPE" == "lunix4k" -o "$BOXTYPE" == "gbquad4k" -o "$BOXTYPE" == "gbue4k" -o "$BOXTYPE" == "spycat4kmini" -o "$BOXTYPE" == "spycat4k" -o "$BOXTYPE" == "spycat4kcombo" -o "$BOXTYPE" == "h7" -o "$BOXTYPE" == "h9" -o "$BOXTYPE" == "h9combo" -o "$BOXTYPE" == "h10" -o "$BOXTYPE" == "sf5008" -o "$BOXTYPE" == "et1x000" -o "$BOXTYPE" == "et13000" -o "$BOXTYPE" == "cc1" -o "$BOXTYPE" == "sf8008" -o "$BOXTYPE" == "hd60" -o "$BOXTYPE" == "hd61" -o "$BOXTYPE" == "i55plus" -o "$BOXTYPE" == "ustym4kpro" -o "$BOXBRAND" == "maxytec" -o "$BOXTYPE" == "viper4k" -o "$BOXTYPE" == "beyonwizv2" -o "$BOXTYPE" == "gbtrio4k" -o "$BOXTYPE" == "gbip4k" -o "$BOXTYPE" == "gbx34k" -o "$BOXTYPE" == "odroidc2" -o "$BOXBRAND" == "rpi" -o "$BOXTYPE" == "beyonwizu4" -o "$BOXTYPE" == "bre2ze4k")

AM_CONDITIONAL(HAVE_CORTEXA9HF, test "$BOXTYPE" == "wetekplay" -o "$BOXTYPE" == "dinoboth265" -o "$BOXTYPE" == "axashistwin" -o "$BOXTYPE" == "anadolprohd5" -o "$BOXTYPE" == "x8hp")

AM_CONDITIONAL(HAVE_AARCH64, test "$BOXTYPE" == "wetekplay2" -o "$BOXTYPE" == "wetekhub" -o "$BOXBRAND" == "linkdroid" -o "$BOXTYPE" == "osmio4k" -o "$BOXTYPE" == "osmio4kplus" -o "$BOXTYPE" == osmini4k -o "$BOXTYPE" == "dreamone")

AC_CONFIG_FILES([
Makefile

AudioEffect/Makefile
AudioEffect/src/Makefile
AudioEffect/meta/Makefile
AudioEffect/po/Makefile

Blindscan/Makefile
Blindscan/src/Makefile
Blindscan/meta/Makefile
Blindscan/po/Makefile

BTDevicesManager/Makefile
BTDevicesManager/src/Makefile
BTDevicesManager/meta/Makefile
BTDevicesManager/po/Makefile

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

DMBlindscan/src/Makefile
DMBlindscan/po/Makefile
DMBlindscan/Makefile
DMBlindscan/meta/Makefile
DMBlindscan/src/images/Makefile

ABMCustomMixImporter/Makefile
ABMCustomMixImporter/meta/Makefile
ABMCustomMixImporter/po/Makefile
ABMCustomMixImporter/src/Makefile
ABMCustomMixImporter/mixes/Makefile

Fempa/Makefile
Fempa/meta/Makefile
Fempa/src/Makefile
Fempa/po/Makefile

FirmwareUpgrade/Makefile
FirmwareUpgrade/src/Makefile
FirmwareUpgrade/meta/Makefile
FirmwareUpgrade/po/Makefile

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

LCD4linux/Makefile
LCD4linux/src/Makefile
LCD4linux/src/data/Makefile
LCD4linux/src/data/Clock1/Makefile
LCD4linux/src/data/Clock2/Makefile
LCD4linux/src/data/Clock3/Makefile
LCD4linux/src/data/Clock4/Makefile
LCD4linux/src/data/Clock5/Makefile
LCD4linux/src/data/Clock6/Makefile
LCD4linux/src/meteo/Makefile
LCD4linux/src/renderer/Makefile
LCD4linux/src/wetter/Makefile
LCD4linux/src/dinobot/Makefile
LCD4linux/src/aarch64/Makefile
LCD4linux/src/armv7a/Makefile
LCD4linux/src/armv7ahf/Makefile
LCD4linux/src/cortexa9hf/Makefile
LCD4linux/src/mips/Makefile
LCD4linux/src/sh4/Makefile
LCD4linux/meta/Makefile
LCD4linux/po/Makefile

MisPlsLcnScan/Makefile
MisPlsLcnScan/images/Makefile
MisPlsLcnScan/lib/Makefile
MisPlsLcnScan/meta/Makefile
MisPlsLcnScan/po/Makefile
MisPlsLcnScan/src/Makefile

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

TerrestrialScan/Makefile
TerrestrialScan/images/Makefile
TerrestrialScan/lib/Makefile
TerrestrialScan/meta/Makefile
TerrestrialScan/po/Makefile
TerrestrialScan/src/Makefile

TransCodingSetup/Makefile
TransCodingSetup/meta/Makefile
TransCodingSetup/po/Makefile
TransCodingSetup/src/Makefile

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

SimpleFanControl/Makefile
SimpleFanControl/src/Makefile
SimpleFanControl/meta/Makefile
SimpleFanControl/po/Makefile

SF8VFDControl/Makefile
SF8VFDControl/src/Makefile
SF8VFDControl/meta/Makefile
SF8VFDControl/po/Makefile

StreamTV/Makefile
StreamTV/src/Makefile
StreamTV/meta/Makefile
StreamTV/po/Makefile
StreamTV/icons/Makefile

VentonFanControl/Makefile
VentonFanControl/src/Makefile
VentonFanControl/meta/Makefile
VentonFanControl/po/Makefile

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

XtrendFanControl/Makefile
XtrendFanControl/src/Makefile
XtrendFanControl/meta/Makefile
XtrendFanControl/po/Makefile

XtrendRemote/Makefile
XtrendRemote/src/Makefile
XtrendRemote/meta/Makefile
XtrendRemote/po/Makefile

])
AC_OUTPUT
