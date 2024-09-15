import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'package:flutter/services.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';
import 'package:sqflite/sqlite_api.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';

class MVCDatabaseProvider {
  final int _version = 3;
  late final String _dbName;
  late final String _sql_create_schema;
  late final Database _db;

  Future<Database> getDatabase() async {
    _dbName = "database.db";
    //   jsonDecode(await rootBundle.loadString("assets/global.json"))["name"];

    _sql_create_schema =
        await rootBundle.loadString("assets/databases/database.sql");

    if (Platform.isWindows || Platform.isLinux) {
      sqfliteFfiInit();
    }
    databaseFactory = databaseFactoryFfi;

    String db_path = join(await getDatabasesPath(), _dbName);
    print(db_path);
    _db =
        await openDatabase(db_path, version: _version, onCreate: (db, version) {
      db.execute(_sql_create_schema);
    });
    return _db;
  }
}
