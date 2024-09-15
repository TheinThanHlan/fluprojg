import 'package:flutter/material.dart';
import '../../mvc_template/interface/IMVCView.dart';
import './ComponentController.dart';

class ComponentPage extends StatelessWidget implements IMVCView {
  late final ComponentController controller;
  @override
  Widget build(BuildContext context) {
    return Text("Hello from Manage Product Page");
  }
}
