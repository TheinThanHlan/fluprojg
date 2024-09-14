import '../interface/IMVCView.dart';

abstract class MVCController {
  //late final IMVCView view;
  //late final IMVCDao dao;
  late final IMVCView view;
  MVCController({required this.view}) {
    view.controller = this;
  }
}
