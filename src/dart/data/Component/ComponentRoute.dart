import '../../mvc_template/injection_container.dart';
import './ComponentPage.dart';
import "./ComponentNav.dart";
import 'package:go_router/go_router.dart';

class ComponentRoute {
  final routeTree = GoRoute(
    builder: (context, state) {
      return getIt<ComponentPage>();
    },

    //this redirect act like route guard
    //if you want to redirect your page to other places by condition decomment this
    //redirect: (context, state) {
    //  if (true) {
    //    return null;
    //  } else {
    //    return null;
    //  }
    //},
    path: "/Component",
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
    //if you want to add static nav please add this
    //builder is ComponentNav
    //route = ShellRoute(builder: ComponentNav, routes: [routeTree]);

    //if you want to create page without nav please un command this
    //builder is ComponentPage
    route = routeTree;
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
