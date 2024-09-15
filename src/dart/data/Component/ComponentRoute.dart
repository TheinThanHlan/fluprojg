import '../../mvc_template/injection_container.dart';
import './ComponentPage.dart';
import "./ComponentNav.dart";
import 'package:go_router/go_router.dart';

class ComponentRoute {
  final routeTree = GoRoute(
    builder: (context, state) {
      return getIt<ComponentPage>();
    },
    path: "Component",
    name: "Component Products",
  );
  /*
    children: [
      TripletNTreeNode<TripletRoute>(
        value: TripletRoute(page: "", uri: "ManageSize", name: "Manage Size"),
      ),
      TripletNTreeNode<TripletRoute>(
        value: TripletRoute(page: "", uri: "ManageType", name: "Manage Type"),
      ),
      TripletNTreeNode<TripletRoute>(
        value: TripletRoute(page: "", uri: "ManagePrice", name: "Manage Price"),
      ),
      TripletNTreeNode<TripletRoute>(
        value: TripletRoute(
            page: "", uri: "ManageCategory", name: "Manage Category"),
      ),
      TripletNTreeNode<TripletRoute>(
        value: TripletRoute(
            page: "", uri: "Component", name: "Manage Product"),
      ),
    ],*/
  late var route;
  ComponentRoute() {
    route = ShellRoute(builder: ComponentNav, routes: [routeTree]);
  }
}




/*
    ShellRoute(
      builder: (BuildContext context, GoRouterState state, Widget child) {
      },
      routes: <RouteBase>[
      ],
    ),
    */
