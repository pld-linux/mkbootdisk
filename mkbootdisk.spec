Summary: Creates an initial ramdisk image for preloading modules.
Name: mkbootdisk
%define version 1.2
Version: %{version}
Release: 2
Copyright: GPL
Group: System Environment/Base
Source: mkbootdisk-%{version}.tar.gz
ExclusiveArch: i386 sparc sparc64
ExclusiveOs: Linux
Requires: mkinitrd
%ifarch sparc sparc64
Requires: silo genromfs
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mkbootdisk program creates a standalone boot floppy disk for booting
the running system.  The created boot disk will look for the root
filesystem on the device mentioned in /etc/fstab and includes an
initial ramdisk image which will load any necessary SCSI modules for
the system.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} BUILDROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) /sbin/mkbootdisk
%attr(644,root,root) /usr/man/man8/mkbootdisk.8
