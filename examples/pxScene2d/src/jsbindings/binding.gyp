{
  "targets": [
    {
      "target_name": "px",
      "sources": [ 

        "jsCallback.cpp",
        "rtWrapperInit.cpp",
        "rtWrapperUtils.cpp",
        "rtFunctionWrapper.cpp",
        "rtObjectWrapper.cpp",

        "../rtObject.cpp",
        "../rtLog.cpp",
        "../rtString.cpp",
        "../rtValue.cpp",
        "../rtFile.cpp",
        "../utf8.c",

        "../pxContextGL.cpp",
        "../pxImage.cpp",
        "../pxImage9.cpp",
        "../pxScene2d.cpp",
        "../pxText.cpp",
        "../pxUtil.cpp",
        "../pxInterpolators.cpp",
        "../pxImageDownloader.cpp"
       ],

      "include_dirs" : [
        "../",
        "../../external/png",
        "../../external/ft/include",
        "../../../../src"
      ],

      "libraries": [
        "-L../../../external/ft/objs/.libs/",
        "-L../../../external/png/.libs",
        "../../../../../build/x11/libpxCore.a",
        "-lX11",
        "-lfreetype",
        "-lglut",
        "-lGLEW",
        "-lpng16",
        "-ljpeg",
        "-lcurl",
#        "-lGL",
#        "-lrt",
      ],

      "cflags": [
        "-DPX_PLATFORM_X11",
        "-DRT_PLATFORM_LINUX",
        "-DENABLE_GLUT",
        "-Wno-attributes"
      ]
    }
  ]
}
