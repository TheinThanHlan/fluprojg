import 'package:flutter/material.dart';
import '../../mvc_template/all.dart';
import './PAGEController.dart';

class Tablet extends StatelessWidget {
  late final PAGEController controller;
  Tablet({required this.controller});

  Widget build(BuildContext context) {
    return Text(controller.greet);
  }

//  State<StatefulWidget> createState() {
//    // TODO: implement createState
//    return _Tablet();
//  }
}

//class _Tablet extends State<Tablet> {
//  @override
//  Widget build(BuildContext context) {
//    // TODO: implement build
//    return Text(widget.controller.greet);
//  }
//}
