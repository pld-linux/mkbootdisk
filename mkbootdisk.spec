Summary:	Creates a standalone boot floppy for the running system
Summary(pl):	Tworzy dyskietk� startow� dla dzia�aj�cego systemu
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
Program mkbootdisk tworzy samodzieln� dyskietk� startow� dla
dzia�aj�cego systemu. Utworzony obraz dyskietki przy starcie b�dzie
szuka� g��wnego systemu plik�w na urz�dzeniu wymienionym w /etc/fstab
i zawiera� bedzie obraz startowego ramdysku �aduj�cego wszelkie
niezb�dnie dla systemu modu�y potrzebne do podmontowania g��wnego
systemu plikowego i kontynuacji z w niego dalej startu systemu.
Program bazuje na lilo, jako �e r�cznie zrobienie dyskietki startowej
do u�ycia z syslinux b�d� grubem nie wymaga �adnych trick�w.

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
