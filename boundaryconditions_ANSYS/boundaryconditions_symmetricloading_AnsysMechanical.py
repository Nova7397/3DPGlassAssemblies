def after_geometry_changed(this, geometry_object):# Do not edit this line
    """
    Called after geometry has been changed.
    Keyword Arguments : 
        this -- the datamodel object instance of the python code object you are currently editing in the tree
        geometry_object -- The geometry
    """

    # To access properties created using the Property Provider, please use the following command.
    # this.GetCustomPropertyByPath("your_property_group_name/your_property_name")

    # To access scoping properties use the following to access geometry scoping and named selection respectively:
    # this.GetCustomPropertyByPath("your_property_group_name/your_property_name/Geometry Selection")
    # this.GetCustomPropertyByPath("your_property_group_name/your_property_name/Named Selection")
    # Loop in reverse to avoid modifying the list while iterating
    
    
    Material1 = 'glass'
    Material2 = 'interlayer'
    glass_ids = []
    interlayer_ids = []
    # Get all bodies in the model
    all_bodies = DataModel.GetObjectsByType(DataModelObjectCategory.Body)
    for i, body in enumerate(all_bodies):
        body.Thickness = Quantity("300 [mm]") #Assign Thickness
        # Assign materials
        if i <= 21:
            body.Material = Material2
            geo_body = body.GetGeoBody()
            glass_ids.append(geo_body.Id)
        else:
            body.Material = Material1
            geo_body = body.GetGeoBody()
            interlayer_ids.append(geo_body.Id)
            
    
    named_selections = ExtAPI.DataModel.Project.Model.NamedSelections
    sel_glass = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_glass.Ids = glass_ids
    glass_named = named_selections.Children[1]
    glass_named.ScopingMethod = GeometryDefineByType.Geometry
    glass_named.Location = sel_glass
    
    # Create Named Selection for interlayer bodies
    sel_inter = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_inter.Ids = interlayer_ids
    inter_named = named_selections.Children[0]
    inter_named.ScopingMethod = GeometryDefineByType.Geometry
    inter_named.Location = sel_inter



    ###SUPPORT Assignment
    #Support Assignment
    #Select the correct faces
    tolerance = 1e-3
    faces_matchingxy = []
    analysis = DataModel.AnalysisByName("Static Structural")
    geo = analysis.GeoData

    for assembly in geo.Assemblies:
        for part in assembly.Parts:
            for body in part.Bodies:
                for face in body.Faces:
                    all_on_xy_plane = True
                    for vertex in face.Vertices:
                        if abs(vertex.Z) > tolerance:
                            all_on_xy_plane = False
                            break
                    if all_on_xy_plane:
                        faces_matchingxy.append(face.Id)

    # Create a selection with these face IDs
    sel_faces = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_faces.Ids = faces_matchingxy

    # Create or assign to a named selection
    face_named = named_selections.Children[2]  # or use AddNamedSelection() to create new
    face_named.ScopingMethod = GeometryDefineByType.Geometry
    face_named.Location = sel_faces
    
    #####SYMMETRY1
    faces_matchingyz = []
    analysis = DataModel.AnalysisByName("Static Structural")
    geo = analysis.GeoData

    for assembly in geo.Assemblies:
        for part in assembly.Parts:
            for body in part.Bodies:
                for face in body.Faces:
                    all_on_yz_plane = True
                    for vertex in face.Vertices:
                        if abs(vertex.X) > tolerance:
                            all_on_yz_plane = False
                            break
                    if all_on_yz_plane:
                        faces_matchingyz.append(face.Id)

    # Create a selection with these face IDs
    sel_faces = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_faces.Ids = faces_matchingyz

    # Create or assign to a named selection
    face_named = named_selections.Children[3]  # or use AddNamedSelection() to create new
    face_named.ScopingMethod = GeometryDefineByType.Geometry
    face_named.Location = sel_faces
    
    #####SYMMETRY2
    faces_matchingxz = []
    analysis = DataModel.AnalysisByName("Static Structural")
    geo = analysis.GeoData

    for assembly in geo.Assemblies:
        for part in assembly.Parts:
            for body in part.Bodies:
                for face in body.Faces:
                    all_on_xz_plane = True
                    for vertex in face.Vertices:
                        if abs(vertex.Y) > tolerance:
                            all_on_xz_plane = False
                            break
                    if all_on_xz_plane:
                        faces_matchingxz.append(face.Id)

    # Create a selection with these face IDs
    sel_faces = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
    sel_faces.Ids = faces_matchingxz

    # Create or assign to a named selection
    face_named = named_selections.Children[4]  # or use AddNamedSelection() to create new
    face_named.ScopingMethod = GeometryDefineByType.Geometry
    face_named.Location = sel_faces

    
    #Solution Assignment
    sol=DataModel.AnalysisByName("Static Structural")
    MaxPrinStressGlass=sol.Solution.Children[2]
    MaxPrinStressGlass.Location=Model.NamedSelections.Children[0]
    MaxPrinStressInt=sol.Solution.Children[3]
    MaxPrinStressInt.Location=Model.NamedSelections.Children[1]
    MinPrinStressGlass=sol.Solution.Children[4]
    MinPrinStressGlass.Location=Model.NamedSelections.Children[0]
    MinPrinStressInt=sol.Solution.Children[5]
    MinPrinStressInt.Location=Model.NamedSelections.Children[1]
    ##Contact Assignment
    
    all_contacts = Model.Connections
    contactgroup = all_contacts.Children[0]

    for i,contact in enumerate(contactgroup.Children):
        contact.ContactType = ContactType.Frictional
        contact.FrictionCoefficient = 0.2
        if i > 96:
            contact.ContactType = ContactType.Frictionless


    pass

geometry_object=Model.Geometry
after_geometry_changed(this, geometry_object)
