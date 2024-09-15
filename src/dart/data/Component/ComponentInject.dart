import './ComponentController.dart';
import './ComponentPage.dart';
import './ComponentRoute.dart';
import 'package:get_it/get_it.dart';

void injectComponent(GetIt getIt) {
  getIt.registerSingleton(ComponentPage());
  getIt.registerSingleton(ComponentRoute());
  getIt.registerSingleton(ComponentController(view: getIt<ComponentPage>()));
  print("\t~>\tComponent injected;");
}
