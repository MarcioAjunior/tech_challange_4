/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "app/api/predict/route";
exports.ids = ["app/api/predict/route"];
exports.modules = {

/***/ "next/dist/compiled/next-server/app-page.runtime.dev.js":
/*!*************************************************************************!*\
  !*** external "next/dist/compiled/next-server/app-page.runtime.dev.js" ***!
  \*************************************************************************/
/***/ ((module) => {

"use strict";
module.exports = require("next/dist/compiled/next-server/app-page.runtime.dev.js");

/***/ }),

/***/ "next/dist/compiled/next-server/app-route.runtime.dev.js":
/*!**************************************************************************!*\
  !*** external "next/dist/compiled/next-server/app-route.runtime.dev.js" ***!
  \**************************************************************************/
/***/ ((module) => {

"use strict";
module.exports = require("next/dist/compiled/next-server/app-route.runtime.dev.js");

/***/ }),

/***/ "../app-render/work-async-storage.external":
/*!*****************************************************************************!*\
  !*** external "next/dist/server/app-render/work-async-storage.external.js" ***!
  \*****************************************************************************/
/***/ ((module) => {

"use strict";
module.exports = require("next/dist/server/app-render/work-async-storage.external.js");

/***/ }),

/***/ "./work-unit-async-storage.external":
/*!**********************************************************************************!*\
  !*** external "next/dist/server/app-render/work-unit-async-storage.external.js" ***!
  \**********************************************************************************/
/***/ ((module) => {

"use strict";
module.exports = require("next/dist/server/app-render/work-unit-async-storage.external.js");

/***/ }),

/***/ "(rsc)/./node_modules/next/dist/build/webpack/loaders/next-app-loader/index.js?name=app%2Fapi%2Fpredict%2Froute&page=%2Fapi%2Fpredict%2Froute&appPaths=&pagePath=private-next-app-dir%2Fapi%2Fpredict%2Froute.ts&appDir=C%3A%5CUsers%5Cmarci%5COneDrive%5CDesktop%5CFIAP%5CPOS%5C4%20FASE%5CTC%5C6_octopus%5Capp&pageExtensions=tsx&pageExtensions=ts&pageExtensions=jsx&pageExtensions=js&rootDir=C%3A%5CUsers%5Cmarci%5COneDrive%5CDesktop%5CFIAP%5CPOS%5C4%20FASE%5CTC%5C6_octopus&isDev=true&tsconfigPath=tsconfig.json&basePath=&assetPrefix=&nextConfigOutput=&preferredRegion=&middlewareConfig=e30%3D!":
/*!***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************!*\
  !*** ./node_modules/next/dist/build/webpack/loaders/next-app-loader/index.js?name=app%2Fapi%2Fpredict%2Froute&page=%2Fapi%2Fpredict%2Froute&appPaths=&pagePath=private-next-app-dir%2Fapi%2Fpredict%2Froute.ts&appDir=C%3A%5CUsers%5Cmarci%5COneDrive%5CDesktop%5CFIAP%5CPOS%5C4%20FASE%5CTC%5C6_octopus%5Capp&pageExtensions=tsx&pageExtensions=ts&pageExtensions=jsx&pageExtensions=js&rootDir=C%3A%5CUsers%5Cmarci%5COneDrive%5CDesktop%5CFIAP%5CPOS%5C4%20FASE%5CTC%5C6_octopus&isDev=true&tsconfigPath=tsconfig.json&basePath=&assetPrefix=&nextConfigOutput=&preferredRegion=&middlewareConfig=e30%3D! ***!
  \***************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   patchFetch: () => (/* binding */ patchFetch),\n/* harmony export */   routeModule: () => (/* binding */ routeModule),\n/* harmony export */   serverHooks: () => (/* binding */ serverHooks),\n/* harmony export */   workAsyncStorage: () => (/* binding */ workAsyncStorage),\n/* harmony export */   workUnitAsyncStorage: () => (/* binding */ workUnitAsyncStorage)\n/* harmony export */ });\n/* harmony import */ var next_dist_server_route_modules_app_route_module_compiled__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! next/dist/server/route-modules/app-route/module.compiled */ \"(rsc)/./node_modules/next/dist/server/route-modules/app-route/module.compiled.js\");\n/* harmony import */ var next_dist_server_route_modules_app_route_module_compiled__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(next_dist_server_route_modules_app_route_module_compiled__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var next_dist_server_route_kind__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! next/dist/server/route-kind */ \"(rsc)/./node_modules/next/dist/server/route-kind.js\");\n/* harmony import */ var next_dist_server_lib_patch_fetch__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! next/dist/server/lib/patch-fetch */ \"(rsc)/./node_modules/next/dist/server/lib/patch-fetch.js\");\n/* harmony import */ var next_dist_server_lib_patch_fetch__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(next_dist_server_lib_patch_fetch__WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var C_Users_marci_OneDrive_Desktop_FIAP_POS_4_FASE_TC_6_octopus_app_api_predict_route_ts__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./app/api/predict/route.ts */ \"(rsc)/./app/api/predict/route.ts\");\n\n\n\n\n// We inject the nextConfigOutput here so that we can use them in the route\n// module.\nconst nextConfigOutput = \"\"\nconst routeModule = new next_dist_server_route_modules_app_route_module_compiled__WEBPACK_IMPORTED_MODULE_0__.AppRouteRouteModule({\n    definition: {\n        kind: next_dist_server_route_kind__WEBPACK_IMPORTED_MODULE_1__.RouteKind.APP_ROUTE,\n        page: \"/api/predict/route\",\n        pathname: \"/api/predict\",\n        filename: \"route\",\n        bundlePath: \"app/api/predict/route\"\n    },\n    resolvedPagePath: \"C:\\\\Users\\\\marci\\\\OneDrive\\\\Desktop\\\\FIAP\\\\POS\\\\4 FASE\\\\TC\\\\6_octopus\\\\app\\\\api\\\\predict\\\\route.ts\",\n    nextConfigOutput,\n    userland: C_Users_marci_OneDrive_Desktop_FIAP_POS_4_FASE_TC_6_octopus_app_api_predict_route_ts__WEBPACK_IMPORTED_MODULE_3__\n});\n// Pull out the exports that we need to expose from the module. This should\n// be eliminated when we've moved the other routes to the new format. These\n// are used to hook into the route.\nconst { workAsyncStorage, workUnitAsyncStorage, serverHooks } = routeModule;\nfunction patchFetch() {\n    return (0,next_dist_server_lib_patch_fetch__WEBPACK_IMPORTED_MODULE_2__.patchFetch)({\n        workAsyncStorage,\n        workUnitAsyncStorage\n    });\n}\n\n\n//# sourceMappingURL=app-route.js.map//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKHJzYykvLi9ub2RlX21vZHVsZXMvbmV4dC9kaXN0L2J1aWxkL3dlYnBhY2svbG9hZGVycy9uZXh0LWFwcC1sb2FkZXIvaW5kZXguanM/bmFtZT1hcHAlMkZhcGklMkZwcmVkaWN0JTJGcm91dGUmcGFnZT0lMkZhcGklMkZwcmVkaWN0JTJGcm91dGUmYXBwUGF0aHM9JnBhZ2VQYXRoPXByaXZhdGUtbmV4dC1hcHAtZGlyJTJGYXBpJTJGcHJlZGljdCUyRnJvdXRlLnRzJmFwcERpcj1DJTNBJTVDVXNlcnMlNUNtYXJjaSU1Q09uZURyaXZlJTVDRGVza3RvcCU1Q0ZJQVAlNUNQT1MlNUM0JTIwRkFTRSU1Q1RDJTVDNl9vY3RvcHVzJTVDYXBwJnBhZ2VFeHRlbnNpb25zPXRzeCZwYWdlRXh0ZW5zaW9ucz10cyZwYWdlRXh0ZW5zaW9ucz1qc3gmcGFnZUV4dGVuc2lvbnM9anMmcm9vdERpcj1DJTNBJTVDVXNlcnMlNUNtYXJjaSU1Q09uZURyaXZlJTVDRGVza3RvcCU1Q0ZJQVAlNUNQT1MlNUM0JTIwRkFTRSU1Q1RDJTVDNl9vY3RvcHVzJmlzRGV2PXRydWUmdHNjb25maWdQYXRoPXRzY29uZmlnLmpzb24mYmFzZVBhdGg9JmFzc2V0UHJlZml4PSZuZXh0Q29uZmlnT3V0cHV0PSZwcmVmZXJyZWRSZWdpb249Jm1pZGRsZXdhcmVDb25maWc9ZTMwJTNEISIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7OztBQUErRjtBQUN2QztBQUNxQjtBQUNrRDtBQUMvSDtBQUNBO0FBQ0E7QUFDQSx3QkFBd0IseUdBQW1CO0FBQzNDO0FBQ0EsY0FBYyxrRUFBUztBQUN2QjtBQUNBO0FBQ0E7QUFDQTtBQUNBLEtBQUs7QUFDTDtBQUNBO0FBQ0EsWUFBWTtBQUNaLENBQUM7QUFDRDtBQUNBO0FBQ0E7QUFDQSxRQUFRLHNEQUFzRDtBQUM5RDtBQUNBLFdBQVcsNEVBQVc7QUFDdEI7QUFDQTtBQUNBLEtBQUs7QUFDTDtBQUMwRjs7QUFFMUYiLCJzb3VyY2VzIjpbIiJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBBcHBSb3V0ZVJvdXRlTW9kdWxlIH0gZnJvbSBcIm5leHQvZGlzdC9zZXJ2ZXIvcm91dGUtbW9kdWxlcy9hcHAtcm91dGUvbW9kdWxlLmNvbXBpbGVkXCI7XG5pbXBvcnQgeyBSb3V0ZUtpbmQgfSBmcm9tIFwibmV4dC9kaXN0L3NlcnZlci9yb3V0ZS1raW5kXCI7XG5pbXBvcnQgeyBwYXRjaEZldGNoIGFzIF9wYXRjaEZldGNoIH0gZnJvbSBcIm5leHQvZGlzdC9zZXJ2ZXIvbGliL3BhdGNoLWZldGNoXCI7XG5pbXBvcnQgKiBhcyB1c2VybGFuZCBmcm9tIFwiQzpcXFxcVXNlcnNcXFxcbWFyY2lcXFxcT25lRHJpdmVcXFxcRGVza3RvcFxcXFxGSUFQXFxcXFBPU1xcXFw0IEZBU0VcXFxcVENcXFxcNl9vY3RvcHVzXFxcXGFwcFxcXFxhcGlcXFxccHJlZGljdFxcXFxyb3V0ZS50c1wiO1xuLy8gV2UgaW5qZWN0IHRoZSBuZXh0Q29uZmlnT3V0cHV0IGhlcmUgc28gdGhhdCB3ZSBjYW4gdXNlIHRoZW0gaW4gdGhlIHJvdXRlXG4vLyBtb2R1bGUuXG5jb25zdCBuZXh0Q29uZmlnT3V0cHV0ID0gXCJcIlxuY29uc3Qgcm91dGVNb2R1bGUgPSBuZXcgQXBwUm91dGVSb3V0ZU1vZHVsZSh7XG4gICAgZGVmaW5pdGlvbjoge1xuICAgICAgICBraW5kOiBSb3V0ZUtpbmQuQVBQX1JPVVRFLFxuICAgICAgICBwYWdlOiBcIi9hcGkvcHJlZGljdC9yb3V0ZVwiLFxuICAgICAgICBwYXRobmFtZTogXCIvYXBpL3ByZWRpY3RcIixcbiAgICAgICAgZmlsZW5hbWU6IFwicm91dGVcIixcbiAgICAgICAgYnVuZGxlUGF0aDogXCJhcHAvYXBpL3ByZWRpY3Qvcm91dGVcIlxuICAgIH0sXG4gICAgcmVzb2x2ZWRQYWdlUGF0aDogXCJDOlxcXFxVc2Vyc1xcXFxtYXJjaVxcXFxPbmVEcml2ZVxcXFxEZXNrdG9wXFxcXEZJQVBcXFxcUE9TXFxcXDQgRkFTRVxcXFxUQ1xcXFw2X29jdG9wdXNcXFxcYXBwXFxcXGFwaVxcXFxwcmVkaWN0XFxcXHJvdXRlLnRzXCIsXG4gICAgbmV4dENvbmZpZ091dHB1dCxcbiAgICB1c2VybGFuZFxufSk7XG4vLyBQdWxsIG91dCB0aGUgZXhwb3J0cyB0aGF0IHdlIG5lZWQgdG8gZXhwb3NlIGZyb20gdGhlIG1vZHVsZS4gVGhpcyBzaG91bGRcbi8vIGJlIGVsaW1pbmF0ZWQgd2hlbiB3ZSd2ZSBtb3ZlZCB0aGUgb3RoZXIgcm91dGVzIHRvIHRoZSBuZXcgZm9ybWF0LiBUaGVzZVxuLy8gYXJlIHVzZWQgdG8gaG9vayBpbnRvIHRoZSByb3V0ZS5cbmNvbnN0IHsgd29ya0FzeW5jU3RvcmFnZSwgd29ya1VuaXRBc3luY1N0b3JhZ2UsIHNlcnZlckhvb2tzIH0gPSByb3V0ZU1vZHVsZTtcbmZ1bmN0aW9uIHBhdGNoRmV0Y2goKSB7XG4gICAgcmV0dXJuIF9wYXRjaEZldGNoKHtcbiAgICAgICAgd29ya0FzeW5jU3RvcmFnZSxcbiAgICAgICAgd29ya1VuaXRBc3luY1N0b3JhZ2VcbiAgICB9KTtcbn1cbmV4cG9ydCB7IHJvdXRlTW9kdWxlLCB3b3JrQXN5bmNTdG9yYWdlLCB3b3JrVW5pdEFzeW5jU3RvcmFnZSwgc2VydmVySG9va3MsIHBhdGNoRmV0Y2gsICB9O1xuXG4vLyMgc291cmNlTWFwcGluZ1VSTD1hcHAtcm91dGUuanMubWFwIl0sIm5hbWVzIjpbXSwiaWdub3JlTGlzdCI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///(rsc)/./node_modules/next/dist/build/webpack/loaders/next-app-loader/index.js?name=app%2Fapi%2Fpredict%2Froute&page=%2Fapi%2Fpredict%2Froute&appPaths=&pagePath=private-next-app-dir%2Fapi%2Fpredict%2Froute.ts&appDir=C%3A%5CUsers%5Cmarci%5COneDrive%5CDesktop%5CFIAP%5CPOS%5C4%20FASE%5CTC%5C6_octopus%5Capp&pageExtensions=tsx&pageExtensions=ts&pageExtensions=jsx&pageExtensions=js&rootDir=C%3A%5CUsers%5Cmarci%5COneDrive%5CDesktop%5CFIAP%5CPOS%5C4%20FASE%5CTC%5C6_octopus&isDev=true&tsconfigPath=tsconfig.json&basePath=&assetPrefix=&nextConfigOutput=&preferredRegion=&middlewareConfig=e30%3D!\n");

/***/ }),

/***/ "(rsc)/./node_modules/next/dist/build/webpack/loaders/next-flight-client-entry-loader.js?server=true!":
/*!******************************************************************************************************!*\
  !*** ./node_modules/next/dist/build/webpack/loaders/next-flight-client-entry-loader.js?server=true! ***!
  \******************************************************************************************************/
/***/ (() => {



/***/ }),

/***/ "(ssr)/./node_modules/next/dist/build/webpack/loaders/next-flight-client-entry-loader.js?server=true!":
/*!******************************************************************************************************!*\
  !*** ./node_modules/next/dist/build/webpack/loaders/next-flight-client-entry-loader.js?server=true! ***!
  \******************************************************************************************************/
/***/ (() => {



/***/ }),

/***/ "(rsc)/./app/api/predict/route.ts":
/*!**********************************!*\
  !*** ./app/api/predict/route.ts ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   POST: () => (/* binding */ POST)\n/* harmony export */ });\nasync function POST(req) {\n    const { date } = await req.json();\n    if (!date) {\n        return new Response(JSON.stringify({\n            error: \"Data não fornecida\"\n        }), {\n            status: 400\n        });\n    }\n    const apiUrl = \"http://localhost:8000/predict\";\n    if (!apiUrl) {\n        throw new Error(\"A variável de ambiente NEXT_PUBLIC_API_MODEL não está definida.\");\n    }\n    const response = await fetch(apiUrl, {\n        method: \"POST\",\n        headers: {\n            \"Content-Type\": \"application/json\"\n        },\n        body: JSON.stringify({\n            \"date\": date\n        })\n    });\n    const predictions = await response.json();\n    return new Response(JSON.stringify(predictions), {\n        status: 200\n    });\n}\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKHJzYykvLi9hcHAvYXBpL3ByZWRpY3Qvcm91dGUudHMiLCJtYXBwaW5ncyI6Ijs7OztBQUFPLGVBQWVBLEtBQUtDLEdBQVk7SUFDbkMsTUFBTSxFQUFFQyxJQUFJLEVBQUUsR0FBRyxNQUFNRCxJQUFJRSxJQUFJO0lBRS9CLElBQUksQ0FBQ0QsTUFBTTtRQUNULE9BQU8sSUFBSUUsU0FDVEMsS0FBS0MsU0FBUyxDQUFDO1lBQUVDLE9BQU87UUFBcUIsSUFDN0M7WUFBRUMsUUFBUTtRQUFJO0lBRWxCO0lBRUEsTUFBTUMsU0FBU0MsK0JBQWlDO0lBRWhELElBQUksQ0FBQ0QsUUFBUTtRQUNYLE1BQU0sSUFBSUksTUFBTTtJQUNsQjtJQUVBLE1BQU1DLFdBQVcsTUFBTUMsTUFBTU4sUUFBUTtRQUNuQ08sUUFBUTtRQUNSQyxTQUFTO1lBQ1AsZ0JBQWdCO1FBQ2xCO1FBQ0FDLE1BQU1iLEtBQUtDLFNBQVMsQ0FBQztZQUFDLFFBQVNKO1FBQUk7SUFDckM7SUFFQSxNQUFNaUIsY0FBYyxNQUFNTCxTQUFTWCxJQUFJO0lBRXZDLE9BQU8sSUFBSUMsU0FDVEMsS0FBS0MsU0FBUyxDQUFDYSxjQUNmO1FBQUVYLFFBQVE7SUFBSTtBQUVsQiIsInNvdXJjZXMiOlsiQzpcXFVzZXJzXFxtYXJjaVxcT25lRHJpdmVcXERlc2t0b3BcXEZJQVBcXFBPU1xcNCBGQVNFXFxUQ1xcNl9vY3RvcHVzXFxhcHBcXGFwaVxccHJlZGljdFxccm91dGUudHMiXSwic291cmNlc0NvbnRlbnQiOlsiZXhwb3J0IGFzeW5jIGZ1bmN0aW9uIFBPU1QocmVxOiBSZXF1ZXN0KSB7XHJcbiAgICBjb25zdCB7IGRhdGUgfSA9IGF3YWl0IHJlcS5qc29uKCk7XHJcbiAgXHJcbiAgICBpZiAoIWRhdGUpIHtcclxuICAgICAgcmV0dXJuIG5ldyBSZXNwb25zZShcclxuICAgICAgICBKU09OLnN0cmluZ2lmeSh7IGVycm9yOiBcIkRhdGEgbsOjbyBmb3JuZWNpZGFcIiB9KSxcclxuICAgICAgICB7IHN0YXR1czogNDAwIH1cclxuICAgICAgKTtcclxuICAgIH1cclxuXHJcbiAgICBjb25zdCBhcGlVcmwgPSBwcm9jZXNzLmVudi5ORVhUX1BVQkxJQ19BUElfTU9ERUw7XHJcblxyXG4gICAgaWYgKCFhcGlVcmwpIHtcclxuICAgICAgdGhyb3cgbmV3IEVycm9yKFwiQSB2YXJpw6F2ZWwgZGUgYW1iaWVudGUgTkVYVF9QVUJMSUNfQVBJX01PREVMIG7Do28gZXN0w6EgZGVmaW5pZGEuXCIpO1xyXG4gICAgfVxyXG4gICAgXHJcbiAgICBjb25zdCByZXNwb25zZSA9IGF3YWl0IGZldGNoKGFwaVVybCwge1xyXG4gICAgICBtZXRob2Q6IFwiUE9TVFwiLFxyXG4gICAgICBoZWFkZXJzOiB7XHJcbiAgICAgICAgXCJDb250ZW50LVR5cGVcIjogXCJhcHBsaWNhdGlvbi9qc29uXCIsXHJcbiAgICAgIH0sXHJcbiAgICAgIGJvZHk6IEpTT04uc3RyaW5naWZ5KHtcImRhdGVcIiA6IGRhdGV9KSwgXHJcbiAgICB9KTtcclxuXHJcbiAgICBjb25zdCBwcmVkaWN0aW9ucyA9IGF3YWl0IHJlc3BvbnNlLmpzb24oKVxyXG5cclxuICAgIHJldHVybiBuZXcgUmVzcG9uc2UoXHJcbiAgICAgIEpTT04uc3RyaW5naWZ5KHByZWRpY3Rpb25zKSxcclxuICAgICAgeyBzdGF0dXM6IDIwMCB9XHJcbiAgICApO1xyXG4gIH1cclxuICAiXSwibmFtZXMiOlsiUE9TVCIsInJlcSIsImRhdGUiLCJqc29uIiwiUmVzcG9uc2UiLCJKU09OIiwic3RyaW5naWZ5IiwiZXJyb3IiLCJzdGF0dXMiLCJhcGlVcmwiLCJwcm9jZXNzIiwiZW52IiwiTkVYVF9QVUJMSUNfQVBJX01PREVMIiwiRXJyb3IiLCJyZXNwb25zZSIsImZldGNoIiwibWV0aG9kIiwiaGVhZGVycyIsImJvZHkiLCJwcmVkaWN0aW9ucyJdLCJpZ25vcmVMaXN0IjpbXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///(rsc)/./app/api/predict/route.ts\n");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = __webpack_require__.X(0, ["vendor-chunks/next"], () => (__webpack_exec__("(rsc)/./node_modules/next/dist/build/webpack/loaders/next-app-loader/index.js?name=app%2Fapi%2Fpredict%2Froute&page=%2Fapi%2Fpredict%2Froute&appPaths=&pagePath=private-next-app-dir%2Fapi%2Fpredict%2Froute.ts&appDir=C%3A%5CUsers%5Cmarci%5COneDrive%5CDesktop%5CFIAP%5CPOS%5C4%20FASE%5CTC%5C6_octopus%5Capp&pageExtensions=tsx&pageExtensions=ts&pageExtensions=jsx&pageExtensions=js&rootDir=C%3A%5CUsers%5Cmarci%5COneDrive%5CDesktop%5CFIAP%5CPOS%5C4%20FASE%5CTC%5C6_octopus&isDev=true&tsconfigPath=tsconfig.json&basePath=&assetPrefix=&nextConfigOutput=&preferredRegion=&middlewareConfig=e30%3D!")));
module.exports = __webpack_exports__;

})();