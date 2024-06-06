Name:       lyrix
Version:    0.1.1
Release:    1
Summary:    display song lyrix in terminal
License:    GPLv3+
URL:        https://github.com/roguexsubmarine/Lyrix
Source0:    https://github.com/roguexsubmarine/Lyrix/release/%{name}-%{version}.tar.gz

Buildrequires:  make
Requires:       bash python python3
Requires:       python
Requires:       python3

BuildArch:      noarch

%description
This is a command line application to scrape song lyrix from web

%prep
%setup -q

%build

%install
cp -rf lyrix_dist %{buildroot}/%{_bindir}/
cp %{name} %{buildroot}/%{_bindir}/	
chmod +x %{buildroot}/%{_bindi}/%{name}

%files

%changelog
* Fri Jun 07 2024 submarine <roguexsubmarine@gmail.com> - 0.1-1
- initial build

