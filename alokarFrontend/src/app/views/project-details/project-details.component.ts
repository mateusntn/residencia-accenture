import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Project } from 'src/app/components/project/project.model';
import { ProjectService } from 'src/app/components/project/project.service';

@Component({
    selector: 'app-project-details',
    templateUrl: './project-details.component.html',
    styleUrls: ['./project-details.component.css']
})
export class ProjectDetailsComponent implements OnInit {

    project: any;

    constructor(private projectService: ProjectService, private router: ActivatedRoute) { }

    ngOnInit(): void {
        const id = this.router.snapshot.paramMap.get('id');
        this.projectService.readByPk(id).subscribe(project => {
            this.project = project;
            console.log(this.project);
        })
    }

}
