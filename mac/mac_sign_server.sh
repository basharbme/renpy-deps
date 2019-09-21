#!/bin/bash

set -e

IDENTITY="$1"
TARBALL="$2"
APP="$3"

security unlock-keychain -p "$(cat ~/.password)"

pushd /tmp
rm -Rf "$APP" || true
tar xf "$TARBALL"

codesign --entitlements="$(dirname $0)/entitlements.plist" --options=runtime --timestamp --verbose -s "$1" -f --deep --no-strict "$APP"

tar cf "signed-$TARBALL" "$APP"
popd
