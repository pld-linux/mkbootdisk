Summary:	Creates a standalone boot floppy for the running system
Summary(pl):	Tworzy dyskietkê startow± dla dzia³aj±cego systemu
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
ExclusiveArch:	%{ix86} sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mkbootdisk program creates a standalone boot floppy disk for booting the
running system. The created boot disk will look for the root filesystem on
the device mentioned in /etc/fstab and ncludes an initial ramdisk image
which will load any necessary modules for mount root file system and
continue from start system.

%description -l pl
Program mkbootdisk tworzy samodzieln± dyskietkê startow± do startow± do
dzia³aj±cego systemu. Utworzony obraz dyskietki przy starcie bêdzie szuka³
g³ównego systemu plików na urz±dzeniu wymienionym w /etc/fstab i zawiera³
bedzie obraz startowego ramdysku ³aduj±cego wszelkie niezbêdnie dla systemu
modu³y potrzebne do podmontowania g³ównego systemu plikowrgo i kontynuacji z
w niego dalej starrtu systemu.

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
