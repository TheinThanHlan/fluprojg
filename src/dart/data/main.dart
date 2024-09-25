import 'package:device_preview/device_preview.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'mvc_template/all.dart';

void main() {
  init().then((x) {
    MaterialApp mainApp = MaterialApp(
      home:#,
      useInheritedMediaQuery:true,
    );

    //run App
    runApp(
      //un comment this if you want to release
      //mainApp
      DevicePreview(builder: (context) => mainApp),
    );
  });
}
