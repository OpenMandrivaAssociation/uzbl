%define snapshot 20090606

Name:		uzbl
Summary:	Web browser following the UNIX philosophy
Version:	0.0
Release:	%mkrel 0.1.%snapshot.2
Source:		%name-%snapshot.tar.bz2
BuildRequires:	gtk2-devel webkitgtk-devel
Provides:	webclient
License:	GPLv3
Group:		Networking/WWW
URL:		http://www.uzbl.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
Uzbl follows the UNIX philosophy - "Write programs that do one thing
and do it well. Write programs to work together. Write programs to handle
text streams, because that is a universal interface."

 * very minimal graphical interface. You only see what you need
 * what is not browsing, is not in uzbl. Things like url changing,
   loading/saving of bookmarks, saving history, downloads, ... are
   handled through external scripts that you write
 * controllable through various means such as fifo and socket files,
   stdin, keyboard and more
 * advanced, customizable keyboard interface with support for modes,
   modkeys, multichars, variables (keywords) etc. (eg you can tweak the
   interface to be vim-like, emacs-like or any-other-program-like)
 * focus on plaintext storage for your data and configs in simple,
   parseable formats
 * Uzbl keeps it simple, and puts you in charge.

%prep
%setup -q -n %name-%snapshot

%build
%make

%install
%{__rm} -Rf %{buildroot}
%makeinstall_std

%{__mkdir_p} %{buildroot}%{_defaultdocdir}/%{name}
echo 'You can find uzbl documentation and example scripts in /usr/share/uzbl' > \
	%{buildroot}%{_defaultdocdir}/%{name}/README

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/%{name}ctrl
%{_datadir}/%{name}
%{_defaultdocdir}/%{name}/README
