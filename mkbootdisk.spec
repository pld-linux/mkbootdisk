Summary:	Creates a standalone boot floppy for the running system
Summary(pl):	Tworzy bootkietk� dla dzia�aj�cego systemu
Name:		mkbootdisk
Version:	2.0
Release:	0
License:	GPL
Group:		Base/Utilities
Group(pl):	Podstawowe/Narz�dzia
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
Program mkbootdisk tworzy samodzieln� bootkietk� do startowania
dzia�aj�cego systemu. Utworzony dysk b�dzie szuka� g��wnego systemu
plik�w na urz�dzeniu wymienionym w %{_sysconfdir}/fstab i zawiera�
obraz startowego ramdysku �aduj�cego wszelkie niezb�dnie dla systemu
modu�y SCSI.

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
