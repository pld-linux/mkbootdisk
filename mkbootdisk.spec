Summary:	Creates a standalone boot floppy for the running system
Summary(pl):	Tworzy dyskietkê startow± dla dzia³aj±cego systemu
Name:		mkbootdisk
Version:	2.0.2
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://mops.uci.agh.edu.pl/~gotar/%{name}-%{version}.tar.bz2
Requires:	/bin/awk
Requires:	e2fsprogs
Requires:	fileutils
Requires:	geninitrd
Requires:	grep
Requires:	mount
Requires:	textutils
%ifarch %{ix86}
Requires:	lilo
%endif
%ifarch sparc sparc64
Requires:	silo
%endif
ExclusiveArch:	%{ix86} sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mkbootdisk program creates a standalone boot floppy disk for
booting the running system. The created bootdisk will look for the
root filesystem on the device mentioned in /etc/fstab and include an
initial ramdisk image which will load any necessary modules for mount
root file system and continue from start system.
This program uses lilo, as manualy making boot floppy with syslinux or
grub doesn't require any magic.

%description -l pl
Program mkbootdisk tworzy samodzieln± dyskietkê startow± dla
dzia³aj±cego systemu. Utworzony obraz dyskietki przy starcie bêdzie
szuka³ g³ównego systemu plików na urz±dzeniu wymienionym w /etc/fstab
i zawiera³ bedzie obraz startowego ramdysku ³aduj±cego wszelkie
niezbêdnie dla systemu modu³y potrzebne do podmontowania g³ównego
systemu plikowego i kontynuacji z w niego dalej startu systemu.
Program bazuje na lilo, jako ¿e rêcznie zrobienie dyskietki startowej
do u¿ycia z syslinux b±d¼ grubem nie wymaga ¿adnych tricków.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_mandir}/man8}

sufix=ix86
%ifarch sparc sparc64
sufix=sparc
%endif
install mkbootdisk.$sufix $RPM_BUILD_ROOT/sbin/mkbootdisk

install mkbootdisk.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/mkbootdisk
%{_mandir}/man8/mkbootdisk.8*
