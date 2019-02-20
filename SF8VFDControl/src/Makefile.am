installdir = $(libdir)/enigma2/python/Plugins/SystemPlugins/SF8VFDControl

install_PYTHON = *.py

if MIPSEL
dist_install_DATA = led7ctrl

install-data-hook:
	chmod +x $(DESTDIR)$(installdir)/led7ctrl
endif
