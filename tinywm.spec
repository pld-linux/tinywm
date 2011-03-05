Summary:	Tiny X Window manager
Summary(pl.UTF-8):	Bardzo mały menadżer okien
Name:		tinywm
Version:	1.3
Release:	1
License:	Public Domain
Group:		X11/Window Managers
Source0:	http://www.incise.org/files/dev/%{name}-%{version}.tgz
# Source0-md5:	8b1c1c3a0615af122b6f9f16ead6a34e
URL:		http://www.incise.org/tinywm.html
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TinyWM is a ridiculously tiny window manager implemented in nearly as
few lines of C as possible, without being obfuscated or entirely
useless. It allows you to move, resize, focus (sloppy), and raise
windows -- that's it! TinyWM's main purpose is to serve as a quick
example of some window manager programming basics.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	PREFIX="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install tinywm $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tinywm
