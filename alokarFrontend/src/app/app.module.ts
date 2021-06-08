import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProjectReadComponent } from './components/project/project-read/project-read.component';
import { HomeComponent } from './views/home/home.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { ProjectCreateComponent } from './components/project/project-create/project-create.component';
import { NavComponent } from './components/template/nav/nav.component';
import { HeaderComponent } from './components/template/header/header.component';
import { ProjectDetailsComponent } from './views/project-details/project-details.component';
import { ProjectAllocationComponent } from './views/project-allocation/project-allocation.component';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatToolbarModule} from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { NgxPaginationModule } from 'ngx-pagination';
import { ProjectUpdateComponent } from './components/project/project-update/project-update.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    NavComponent,   
    ProjectReadComponent,
    HomeComponent,
    DashboardComponent,
    ProjectCreateComponent,
    ProjectDetailsComponent,
    ProjectAllocationComponent,
    ProjectUpdateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatSidenavModule,
    MatListModule,
    MatButtonModule,
    MatCardModule,
    MatFormFieldModule,
    MatSnackBarModule,
    HttpClientModule,
    FormsModule,
    MatInputModule,
    NgxPaginationModule,
    ReactiveFormsModule
  ],
  providers: [ ],
  bootstrap: [AppComponent]
})
export class AppModule { }
