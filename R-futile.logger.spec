#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-futile.logger
Version  : 1.4.3
Release  : 9
URL      : https://cran.r-project.org/src/contrib/futile.logger_1.4.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/futile.logger_1.4.3.tar.gz
Summary  : A Logging Utility for R
Group    : Development/Tools
License  : LGPL-3.0
Requires: R-futile.options
Requires: R-lambda.r
BuildRequires : R-futile.options
BuildRequires : R-lambda.r
BuildRequires : clr-R-helpers

%description
log4j, futile.logger takes advantage of R idioms to make logging a
    convenient and easy to use replacement for cat and print statements.

%prep
%setup -q -c -n futile.logger

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521228251

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521228251
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library futile.logger
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library futile.logger
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library futile.logger
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library futile.logger|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/futile.logger/DESCRIPTION
/usr/lib64/R/library/futile.logger/INDEX
/usr/lib64/R/library/futile.logger/Meta/Rd.rds
/usr/lib64/R/library/futile.logger/Meta/features.rds
/usr/lib64/R/library/futile.logger/Meta/hsearch.rds
/usr/lib64/R/library/futile.logger/Meta/links.rds
/usr/lib64/R/library/futile.logger/Meta/nsInfo.rds
/usr/lib64/R/library/futile.logger/Meta/package.rds
/usr/lib64/R/library/futile.logger/NAMESPACE
/usr/lib64/R/library/futile.logger/R/futile.logger
/usr/lib64/R/library/futile.logger/R/futile.logger.rdb
/usr/lib64/R/library/futile.logger/R/futile.logger.rdx
/usr/lib64/R/library/futile.logger/help/AnIndex
/usr/lib64/R/library/futile.logger/help/aliases.rds
/usr/lib64/R/library/futile.logger/help/futile.logger.rdb
/usr/lib64/R/library/futile.logger/help/futile.logger.rdx
/usr/lib64/R/library/futile.logger/help/paths.rds
/usr/lib64/R/library/futile.logger/html/00Index.html
/usr/lib64/R/library/futile.logger/html/R.css
