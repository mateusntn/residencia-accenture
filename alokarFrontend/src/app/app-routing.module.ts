import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ProjectCrudComponent } from './views/project-crud/project-crud.component'

const routes: Routes = [
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
