import './MVCDatabaseProvider.dart';
import 'package:get_it/get_it.dart';
import 'package:sqflite/sqflite.dart';

final GetIt getIt = GetIt.I;
void init_injection_container() {
  getIt.registerSingletonAsync<Database>(
      () async => await MVCDatabaseProvider().getDatabase());

  //add injections
}
