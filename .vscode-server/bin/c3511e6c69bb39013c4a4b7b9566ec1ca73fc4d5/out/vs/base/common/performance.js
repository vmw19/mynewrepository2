"use strict";(function(){function f(e){const r=[];typeof e=="number"&&r.push("code/timeOrigin",e);function n(o){r.push(o,Date.now())}function m(){const o=[];for(let i=0;i<r.length;i+=2)o.push({name:r[i],startTime:r[i+1]});return o}return{mark:n,getMarks:m}}function c(){if(typeof performance=="object"&&typeof performance.mark=="function"&&!performance.nodeTiming)return typeof performance.timeOrigin!="number"&&!performance.timing?f():{mark(e){performance.mark(e)},getMarks(){let e=performance.timeOrigin;typeof e!="number"&&(e=performance.timing.navigationStart||performance.timing.redirectStart||performance.timing.fetchStart);const r=[{name:"code/timeOrigin",startTime:Math.round(e)}];for(const n of performance.getEntriesByType("mark"))r.push({name:n.name,startTime:Math.round(e+n.startTime)});return r}};if(typeof process=="object"){const e=Math.round((require.nodeRequire||require)("perf_hooks").performance.timeOrigin);return f(e)}else return console.trace("perf-util loaded in UNKNOWN environment"),f()}function a(e){return e.MonacoPerformanceMarks||(e.MonacoPerformanceMarks=c()),e.MonacoPerformanceMarks}var t;typeof global=="object"?t=global:typeof self=="object"?t=self:t={},typeof define=="function"?define([],function(){return a(t)}):typeof module=="object"&&typeof module.exports=="object"?module.exports=a(t):(console.trace("perf-util defined in UNKNOWN context (neither requirejs or commonjs)"),t.perf=a(t))})();

//# sourceMappingURL=https://ticino.blob.core.windows.net/sourcemaps/c3511e6c69bb39013c4a4b7b9566ec1ca73fc4d5/core/vs/base/common/performance.js.map
