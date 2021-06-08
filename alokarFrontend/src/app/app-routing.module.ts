import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './views/home/home.component'
import { ProjectCreateComponent } from './components/project/project-create/project-create.component';
import { ProjectDetailsComponent } from './views/project-details/project-details.component';
import { ProjectAllocationComponent } from './views/project-allocation/project-allocation.component';
import { ProjectReadComponent } from './components/project/project-read/project-read.component';
import { ProjectUpdateComponent } from './components/project/project-update/project-update.component';

const routes: Routes = [
  {
    path: "",
    component: HomeComponent
  },
  {
    path: "projects",
    component: ProjectReadComponent
  },
  {
    path: "projects/create",
    component: ProjectCreateComponent
  }, 
  {
    path: "projects/details/:id",
    component: ProjectDetailsComponent
  },
  {
    path: "projects/allocation/:id",
    component: ProjectAllocationComponent
  },
  {
      path: "projects/update/:id",
      component: ProjectUpdateComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
