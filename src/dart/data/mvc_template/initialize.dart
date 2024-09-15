import 'package:flutter/widgets.dart';

import './all.dart';

Future<void> init() async {
  await WidgetsFlutterBinding.ensureInitialized();
  init_injection_container();
  await getIt.allReady();
}
