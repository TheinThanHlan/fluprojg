//import 'package:general_pos/views/Auth/AuthInject.dart';

import 'package:go_router/go_router.dart';
import './MVCDatabaseProvider.dart';
import 'package:get_it/get_it.dart';
import 'package:sqflite/sqflite.dart';

final GetIt getIt = GetIt.I;
void init_injection_container() {
  getIt.registerSingletonAsync<Database>(
      () async => await MVCDatabaseProvider().getDatabase());
  //getIt.registerSingleton<GoRouter>(goRouter);
  getIt.registerSingleton(GoRouter(
    initialLocation: "/Auth",
    routes: [],
  ));

  //add injections
  //injectAuth(getIt, getIt<GoRouter>());
}
