"use strict";(self.webpackChunk_coreui_coreui_free_react_admin_template=self.webpackChunk_coreui_coreui_free_react_admin_template||[]).push([[485],{43518:function(e,t,n){n(72791);var s=n(80184);t.Z=function(e){return(0,s.jsxs)(s.Fragment,{children:[e.onView?(0,s.jsx)("i",{className:"fa-solid fa-eye pointer me-2 text-info",onClick:e.onView}):"",(0,s.jsx)("i",{className:"fa-solid fa-trash pointer text-danger",onClick:e.onDelete}),(0,s.jsx)("i",{className:"fa-solid fa-pen-to-square pointer ms-2 text-warning",onClick:e.onEdit})]})}},57653:function(e,t,n){n.r(t),n.d(t,{default:function(){return j}});var s=n(1413),r=n(74165),a=n(15861),c=n(70885),o=n(72791),i=n(43513),l=n(83442),u=n(43518),d=n(9085),m=n(78983),p=n(16871),f=n(43504),h=n.p+"static/media/template.fdcfd54a8d428c36d3b2.xlsx",x=n(80184),j=function(){var e=(0,p.s0)(),t=o.useState([]),n=(0,c.Z)(t,2),j=n[0],g=n[1],v=o.useState({per_page:10,page_number:1}),w=(0,c.Z)(v,2),b=w[0],Z=w[1],N=o.useState({search:"",status:""}),y=(0,c.Z)(N,2),_=y[0],S=y[1],C=o.useState(!0),k=(0,c.Z)(C,2),A=k[0],E=k[1],O=o.useState(0),T=(0,c.Z)(O,2),P=T[0],D=T[1],F=[{name:"Id",selector:function(e){return e.id},sortable:!0},{name:"Name",selector:function(e){return e.name},sortable:!0},{name:"Jurisdiction",selector:function(e){return e.jurisdiction},sortable:!0},{name:"Address",selector:function(e){return e.address},sortable:!0},{name:"Status",selector:function(e){return(0,x.jsx)("span",{className:"status-".concat(e.status),children:e.status})},sortable:!0},{name:"Last Modified",selector:function(e){return new Date(e.updated_at).toLocaleString()},sortable:!0},{name:"Action",selector:function(e){return(0,x.jsx)(u.Z,{onView:function(){return I(e)},onEdit:function(){return q(e)},onDelete:function(){return L(e.id)}})},sortable:!0}],I=function(t){console.log(t),e("/crossings/view",{state:t})},q=function(t){e("/crossings/edit",{state:t})},L=function(){var e=(0,a.Z)((0,r.Z)().mark((function e(t){var n,s;return(0,r.Z)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n=l.Z.deleteCrossing+t,e.next=3,fetch(n,{method:"GET",headers:{Authorization:(0,l.k)()}});case 3:return s=e.sent,e.next=6,s.json();case 6:200===e.sent.status&&(E(!A),d.Am.success("Record deleted successfully!"));case 8:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),R=function(){var e=(0,a.Z)((0,r.Z)().mark((function e(){var t,n,s,a,c,o,i,u;return(0,r.Z)().wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=document.querySelector(".import-form"),n=l.Z.crossingsImport,e.next=4,fetch(n,{method:"POST",headers:{Authorization:(0,l.k)()},body:new FormData(t)});case 4:return s=e.sent,e.next=7,s.json();case 7:a=e.sent,c=a.data,o=c.errors,i=c.success,u=c.warnings,o.forEach((function(e){d.Am.error(e)})),u.forEach((function(e){d.Am.warning(e)})),i&&d.Am.success(i+" Imported Seccessfully");case 12:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}();return o.useEffect((function(){var e=l.Z.crossings;(0,a.Z)((0,r.Z)().mark((function t(){var n,s;return(0,r.Z)().wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,fetch(e+"?per_page=".concat(b.per_page,"&page_number=").concat(b.page_number,"&search=").concat(_.search,"&status=").concat(_.status),{method:"GET",headers:{Authorization:(0,l.k)()}});case 2:return n=t.sent,t.next=5,n.json();case 5:s=t.sent,g(s.data),D(s.total);case 8:case"end":return t.stop()}}),t)})))()}),[b,A,_]),(0,x.jsxs)(x.Fragment,{children:[(0,x.jsx)(d.Ix,{position:"top-right",theme:"colored",autoClose:5e3,hideProgressBar:!1,newestOnTop:!1,closeOnClick:!0,rtl:!1,pauseOnFocusLoss:!0,draggable:!0,pauseOnHover:!0}),(0,x.jsx)(m.xH,{className:"my-2",children:(0,x.jsxs)(m.sl,{children:[(0,x.jsxs)("div",{className:"row",children:[(0,x.jsx)("div",{className:"col-md-6",children:(0,x.jsx)("h5",{className:"d-inline text-uppercase",children:"All Crossings"})}),(0,x.jsx)("div",{className:"col-md-6",children:(0,x.jsxs)("div",{className:"float-end d-inline-flex justify-content-between",children:[(0,x.jsx)("label",{htmlFor:"file",type:"submit",color:"primary",className:"btn btn-primary m-2",children:"Import"}),(0,x.jsx)(f.rU,{to:"/crossings/add",className:"btn text-uppercase btn-primary m-2",children:"Add"})]})})]}),(0,x.jsx)("a",{className:"text-reset",download:"template.xlsx",href:h,children:"Download Excel Template"})]})}),(0,x.jsx)(m.xH,{className:"my-2",children:(0,x.jsx)(m.sl,{children:(0,x.jsxs)("div",{className:"row",children:[(0,x.jsx)("div",{className:"col-5",children:(0,x.jsx)(m.jO,{type:"text",placeholder:"Search..",className:"search-text"})}),(0,x.jsx)("div",{className:"col-5",children:(0,x.jsxs)(m.LX,{className:"search-status",children:[(0,x.jsx)("option",{hidden:!0,value:"",children:"Select"}),(0,x.jsx)("option",{value:"0",children:"Closed"}),(0,x.jsx)("option",{value:"1",children:"Open"}),(0,x.jsx)("option",{value:"2",children:"Caution"})]})}),(0,x.jsx)("div",{className:"col-2",children:(0,x.jsx)(m.u5,{type:"button",className:"float-end w-100",color:"primary",onClick:function(){var e=document.querySelector(".search-text").value,t=document.querySelector(".search-status").value;S({search:e,status:t})},children:"Search"})})]})})}),(0,x.jsx)(i.ZP,{columns:F,data:j,pagination:!0,onSelectedRowsChange:function(){},paginationServer:!0,paginationTotalRows:P,onChangeRowsPerPage:function(e){return Z((0,s.Z)((0,s.Z)({},b),{},{per_page:e}))},onChangePage:function(e,t){return Z((0,s.Z)((0,s.Z)({},b),{},{page_number:e}))}}),(0,x.jsx)("form",{encType:"multipart/from-data",className:"d-none import-form",children:(0,x.jsx)("input",{type:"file",name:"file",id:"file",accept:".xlsx",onChange:R})})]})}}}]);
//# sourceMappingURL=485.a557db54.chunk.js.map