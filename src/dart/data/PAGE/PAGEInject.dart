import './PAGEController.dart';
import './PAGEPage.dart';
import 'package:get_it/get_it.dart';

void injectPAGE(GetIt getIt) {
  getIt.registerSingleton(PAGEPage());
  getIt.registerSingleton(PAGEController(view: getIt<PAGEPage>()));
  print("\t~>\tPAGE injected;");
}
