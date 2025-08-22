#!/bin/bash

set +x

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

BUILD_DIR="$SCRIPT_DIR"/build

cmake -E make_directory "$BUILD_DIR"


build_app()
{
  # cd "$BUILD_DIR" || exit
  pushd "$BUILD_DIR"

  cmake "$SCRIPT_DIR" -DCMAKE_INSTALL_PREFIX="$SCRIPT_DIR/data"

  cmake --build . -j "$(nproc)"
  if [ $? -ne 0 ]; then
    exit 1
  fi
  cmake --install .
  popd
}


build_app
sleep 1
build_app

rm -rf "$BUILD_DIR/"
echo
echo "### Build done"
echo
