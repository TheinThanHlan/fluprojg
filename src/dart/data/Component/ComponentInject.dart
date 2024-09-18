import './ComponentController.dart';
import './ComponentPage.dart';
import './ComponentRoute.dart';
import 'package:get_it/get_it.dart';
import 'package:go_router/go_router.dart';

void injectComponent(GetIt getIt) {
  getIt.registerSingleton(ComponentPage());
  getIt.registerSingleton(ComponentRoute());
  getIt.registerSingleton(ComponentController(view: getIt<ComponentPage>()));
  getIt<GoRouter>().configuration.routes.add(getIt<ComponentRoute>().route);
  print("\t~>\tComponent injected;");
}
