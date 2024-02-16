# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

Name: python-scikit-learn
Epoch: 100
Version: 1.5.1
Release: 1%{?dist}
Summary: Python module for machine learning
License: BSD-3-Clause
URL: https://github.com/scikit-learn/scikit-learn/tags
Source0: %{name}_%{version}.orig.tar.gz
Source99: %{name}.rpmlintrc
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-joblib >= 1.2.0
BuildRequires: python3-meson-python >= 0.15.0
BuildRequires: python3-numpy >= 1.19.5
BuildRequires: python3-numpy-f2py >= 1.19.5
BuildRequires: python3-scipy >= 1.6.0
BuildRequires: python3-setuptools
BuildRequires: python3-threadpoolctl >= 3.1.0

%description
Scikit-learn is an open source machine learning library that supports
supervised and unsupervised learning. It also provides various tools for
model fitting, data preprocessing, model selection, model evaluation,
and many other utilities.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-scikit-learn
Summary: Python module for machine learning
Requires: python3
Provides: python3-scikit-learn = %{epoch}:%{version}-%{release}
Provides: python3dist(scikit-learn) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-scikit-learn = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(scikit-learn) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-scikit-learn = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(scikit-learn) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-scikit-learn
Scikit-learn is an open source machine learning library that supports
supervised and unsupervised learning. It also provides various tools for
model fitting, data preprocessing, model selection, model evaluation,
and many other utilities.

%files -n python%{python3_version_nodots}-scikit-learn
%license COPYING
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-scikit-learn
Summary: Python module for machine learning
Requires: python3
Provides: python3-scikit-learn = %{epoch}:%{version}-%{release}
Provides: python3dist(scikit-learn) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-scikit-learn = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(scikit-learn) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-scikit-learn = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(scikit-learn) = %{epoch}:%{version}-%{release}

%description -n python3-scikit-learn
Scikit-learn is an open source machine learning library that supports
supervised and unsupervised learning. It also provides various tools for
model fitting, data preprocessing, model selection, model evaluation,
and many other utilities.

%files -n python3-scikit-learn
%license COPYING
%{python3_sitearch}/*
%endif

%changelog
