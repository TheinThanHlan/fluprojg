import './COMPONENTComponent.dart';
import './COMPONENTModel.dart';
import 'package:get_it/get_it.dart';

void injectCOMPONENT(GetIt getIt) {
  getIt.registerSingleton(COMPONENTComponent());
  print("\t~>\tCOMPONENT injected;");
}
