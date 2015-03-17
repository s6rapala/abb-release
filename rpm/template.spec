Name:           ros-hydro-abb
Version:        1.1.6
Release:        0%{?dist}
Summary:        ROS abb package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/abb
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-abb-common
Requires:       ros-hydro-abb-driver
Requires:       ros-hydro-abb-irb2400-moveit-config
Requires:       ros-hydro-abb-irb2400-moveit-plugins
Requires:       ros-hydro-abb-irb2400-support
Requires:       ros-hydro-abb-irb5400-support
Requires:       ros-hydro-abb-irb6600-support
Requires:       ros-hydro-abb-irb6640-moveit-config
Requires:       ros-hydro-abb-moveit-plugins
Requires:       ros-hydro-irb-2400-moveit-config
Requires:       ros-hydro-irb-6640-moveit-config
BuildRequires:  ros-hydro-catkin

%description
ROS-Industrial support for ABB manipulators (metapackage).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Mar 17 2015 Shaun Edwards <shaun.edwards@gmail.com> - 1.1.6-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Shaun Edwards <shaun.edwards@gmail.com> - 1.1.5-0
- Autogenerated by Bloom

* Sat Dec 27 2014 Shaun Edwards <shaun.edwards@gmail.com> - 1.1.4-0
- Autogenerated by Bloom

