Summary:	Creates a standalone boot floppy for the running system
Summary(es):	Crea un disquete de arranque
Summary(pl):	Tworzy dyskietkЙ startow╠ dla dziaЁaj╠cego systemu
Summary(pt_BR):	Cria um disco de inicializaГЦo
Summary(ru):	Создает самодостаточную загрузочную дискету для текущей системы
Summary(uk):	Створю╓ самодостатню загрузочну дискету для поточно╖ системи
Name:		mkbootdisk
Version:	2.0.3
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://mops.uci.agh.edu.pl/~gotar/programs/sh/%{name}-%{version}.tar.bz2
# Source0-md5:	25128bfc5fa2d68031f3abebb0a2a424
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
root file system and continue from start system. This program uses
lilo, as manualy making boot floppy with syslinux or grub doesn't
require any magic.

%description -l es
Este paquete crea un disco de arranque autocontenido. Asume que el
disco de arranque debe usar la particiСn raМz configurada en el
archivo /etc/fstab. El disco de arranque obtenido incluye todos los
mСdulos SCSI necesarios al sistema.

%description -l pl
Program mkbootdisk tworzy samodzieln╠ dyskietkЙ startow╠ dla
dziaЁaj╠cego systemu. Utworzony obraz dyskietki przy starcie bЙdzie
szukaЁ gЁСwnego systemu plikСw na urz╠dzeniu wymienionym w /etc/fstab
i zawieraЁ bedzie obraz startowego ramdysku Ёaduj╠cego wszelkie
niezbЙdnie dla systemu moduЁy potrzebne do podmontowania gЁСwnego
systemu plikowego i kontynuacji z w niego dalej startu systemu.
Program bazuje na lilo, jako ©e rЙcznie zrobienie dyskietki startowej
do u©ycia z syslinux b╠d╪ grubem nie wymaga ©adnych trickСw.

%description -l pt_BR
Este pacote cria um disco de inicializaГЦo auto-contido. Assume que o
disco de inicializaГЦo deve usar a partiГЦo raiz configurada no
arquivo /etc/fstab. O disco de inicializaГЦo resultando inclui todos
os mСdulos SCSI necessАrios ao sistema.

%description -l ru
Программа mkbootdisk создает самодостаточную загрузочную дискету для
загрузки текущей системы. Созданная дискетка будет искать корневую
файловую систему на устройстве, указанном в /etc/fstab, и включает
начальный образ ramdisk'а, который будет загружать модули SCSI, IDE и
файловых систем, необходимые для монтирования корневой файловой
системы.

%description -l uk
Програма mkbootdisk створю╓ самодостатню загрузочну дискету для
загрузки поточно╖ системи. Створена дискета буде шукати корньову
файлову систему на пристро╖, зазначеному у /etc/fstab, ╕ м╕стить
початковий образ ramdisk'у, котрий буде загружати модул╕ SCSI, IDE та
файлових систем, необх╕дн╕ для монтування корньово╖ файлово╖ системи.

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
