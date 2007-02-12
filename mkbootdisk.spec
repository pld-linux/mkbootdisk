Summary:	Creates a standalone boot floppy for the running system
Summary(es.UTF-8):   Crea un disquete de arranque
Summary(pl.UTF-8):   Tworzy dyskietkę startową dla działającego systemu
Summary(pt_BR.UTF-8):   Cria um disco de inicialização
Summary(ru.UTF-8):   Создает самодостаточную загрузочную дискету для текущей системы
Summary(uk.UTF-8):   Створює самодостатню загрузочну дискету для поточної системи
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

%description -l es.UTF-8
Este paquete crea un disco de arranque autocontenido. Asume que el
disco de arranque debe usar la partición raíz configurada en el
archivo /etc/fstab. El disco de arranque obtenido incluye todos los
módulos SCSI necesarios al sistema.

%description -l pl.UTF-8
Program mkbootdisk tworzy samodzielną dyskietkę startową dla
działającego systemu. Utworzony obraz dyskietki przy starcie będzie
szukał głównego systemu plików na urządzeniu wymienionym w /etc/fstab
i zawierał będzie obraz startowego ramdysku ładującego wszelkie
niezbędnie dla systemu moduły potrzebne do podmontowania głównego
systemu plikowego i kontynuacji z w niego dalej startu systemu.
Program bazuje na lilo, jako że ręcznie zrobienie dyskietki startowej
do użycia z syslinux bądź grubem nie wymaga żadnych tricków.

%description -l pt_BR.UTF-8
Este pacote cria um disco de inicialização auto-contido. Assume que o
disco de inicialização deve usar a partição raiz configurada no
arquivo /etc/fstab. O disco de inicialização resultando inclui todos
os módulos SCSI necessários ao sistema.

%description -l ru.UTF-8
Программа mkbootdisk создает самодостаточную загрузочную дискету для
загрузки текущей системы. Созданная дискетка будет искать корневую
файловую систему на устройстве, указанном в /etc/fstab, и включает
начальный образ ramdisk'а, который будет загружать модули SCSI, IDE и
файловых систем, необходимые для монтирования корневой файловой
системы.

%description -l uk.UTF-8
Програма mkbootdisk створює самодостатню загрузочну дискету для
загрузки поточної системи. Створена дискета буде шукати корньову
файлову систему на пристрої, зазначеному у /etc/fstab, і містить
початковий образ ramdisk'у, котрий буде загружати модулі SCSI, IDE та
файлових систем, необхідні для монтування корньової файлової системи.

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
