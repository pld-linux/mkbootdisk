Summary:	Creates a standalone boot floppy for the running system
Summary(pl):	Tworzy bootkietkê dla dzia³aj±cego systemu
Name:		mkbootdisk
Version:	2.0
Release:	0
License:	GPL
Group:		Base/Utilities
Group(pl):	Podstawowe/Narzêdzia
Source:		%{name}-%{version}.tar.gz
ExclusiveArch:	i386 sparc sparc64
Requires:	mkinitrd
%ifarch sparc sparc64
Requires:	silo genromfs
%endif
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

%install
rm -rf $RPM_BUILD_ROOT
%{__make} BUILDROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/mkbootdisk
%attr(644,root,root) %{_mandir}/man8/mkbootdisk.8
