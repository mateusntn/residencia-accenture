import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ProjectCrudComponent } from './views/project-crud/project-crud.component';
import { HomeComponent } from './views/home/home.component'
import { ProjectCreateComponent } from './components/project/project-create/project-create.component';
import { ProjectDetailsComponent } from './views/project-details/project-details.component';

const routes: Routes = [
  {
    path: "",
    component: HomeComponent
  },
  {
    path: "projects",
    component: ProjectCrudComponent
  },
  {
    path: "projects/create",
    component: ProjectCreateComponent
  }, 
  {
    path: "projects/details",
    component: ProjectDetailsComponent
  } 

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
