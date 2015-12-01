%define    name doctor

Name:      %{name}
Version:   1.0.0
Release:   1
BuildArch: x86_64
Summary:   A small utility providing an extensible system to check your server's health.
Group:     Applications/System
Source0:   %{name}.tar.gz
License:   MIT License

%description
%{summary}

%prep
%setup -q -n src

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p  %{buildroot}
%{__cp} -a * %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/doctor.%{name}
%{_bindir}/%{name}

%changelog
* Fri Sep 18 2015 William Garcia <garcia.rodriguez.william@gmail.com> - 1.0.0%{?dist}
- Initial package


