import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ProjectCrudComponent } from './views/project-crud/project-crud.component';
import { HomeComponent } from './views/home/home.component'

const routes: Routes = [
  {
    path: "",
    component: HomeComponent
  },
  {
    path: "projects",
    component: ProjectCrudComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
