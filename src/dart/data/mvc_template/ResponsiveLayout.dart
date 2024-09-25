import 'package:flutter/material.dart';

Widget responsiveLayout({
  required BuildContext context,
  required Widget desktop,
  required Widget mobile,
}) {
  double width = MediaQuery.of(context).size.width;
  if (width <= 800) {
    return mobile;
  } else {
    return desktop;
  }
}
