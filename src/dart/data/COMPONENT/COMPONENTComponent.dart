import 'package:flutter/material.dart';
import './COMPONENTModel.dart';
import '../../../mvc_template/all.dart';
import './Mobile.dart';
import './Desktop.dart';
import './Tablet.dart';

class COMPONENTComponent extends StatelessWidget {
  late COMPONENTModel data;
  COMPONENTComponent setData(COMPONENTModel data) {
    this.data = data;
    return this;
  }

  @override
  Widget build(BuildContext context) {
    return responsiveLayout(
        context: context,
        desktop: Desktop(data: this.data),
        mobile: Mobile(data: this.data),
        tablet: Tablet(data: this.data));
  }
}
