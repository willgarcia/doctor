#!/bin/bash

CWD=$(pwd)
SPEC="doctor.spec"

which rpmbuild > /dev/null
if [ $? -ne 0 ]; then
  echo "Aborting. Cannot continue without rpmbuild from the rpm-build package."
  exit 1
fi

echo "Creating sources archive..."
mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS,tmp}
tar -czvf "doctor.tar.gz" "src/"
mv doctor.tar.gz rpmbuild/SOURCES/

echo "Building RPM..."
rpmbuild  --define "_topdir ${CWD}/rpmbuild" -ba doctor.spec
