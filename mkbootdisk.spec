Summary:	Creates a standalone boot floppy for the running system
Summary(pl):	Tworzy bootkietkê dla dzia³aj±cego systemu
Name:		mkbootdisk
Version:	2.0
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}.ix86.patch
Patch1:		%{name}.sparc.patch
Requires:	geninitrd
%ifarch sparc sparc64
Requires:	silo
%endif
Requires:	geninitrd
ExclusiveArch:	%{ix86} sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mkbootdisk program creates a standalone boot floppy disk for
booting the running system. The created boot disk will look for the
root filesystem on the device mentioned in %{_sysconfdir}/fstab and
ncludes an initial ramdisk image which will load any necessary SCSI
modules for the system.

%description -l pl
Program mkbootdisk tworzy samodzieln± bootkietkê do startowania
dzia³aj±cego systemu. Utworzony dysk bêdzie szuka³ g³ównego systemu
plików na urz±dzeniu wymienionym w %{_sysconfdir}/fstab i zawiera³
obraz startowego ramdysku ³aduj±cego wszelkie niezbêdnie dla systemu
modu³y SCSI.

%prep
%setup -q

%ifarch %{ix86}
%patch0 -p0
%endif

%ifarch sparc sparc64
%patch1 -p0
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install BUILDROOT=$RPM_BUILD_ROOT

install mkbootdisk.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/mkbootdisk
%{_mandir}/man8/mkbootdisk.8*
