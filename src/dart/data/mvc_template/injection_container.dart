//import 'package:general_pos/views/Auth/AuthInject.dart';

import 'package:go_router/go_router.dart';
import './MVCDatabaseProvider.dart';
import 'package:get_it/get_it.dart';
import 'package:sqflite/sqflite.dart';
import '../data/InjectData.dart';

final GetIt getIt = GetIt.I;
Future<void> init_injection_container() async {
  //getIt.registerSingletonAsync<Database>(
  //    () async => await MVCDatabaseProvider().getDatabase());
  //getIt.registerSingleton<GoRouter>(goRouter);
  //getIt.registerSingleton(GoRouter(
  //  initialLocation: "/Auth",
  //  routes: [],
  //));

  getIt.registerSingleton(await MVCDatabaseProvider().getDatabase());
  injectData(getIt);
  await initPages();
  await initComponents();
}

Future<void> initPages() async {}

Future<void> initComponents() async {}
