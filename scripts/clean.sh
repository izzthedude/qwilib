EGG="./qwilib.egg-info"
if [ -d $EGG ]; then
    rm -r $EGG
fi

BUILD="./build"
if [ -d $BUILD ]; then
    rm -r $BUILD
fi

DIST="./dist"
if [ -d $DIST ]; then
    rm -r $DIST
fi