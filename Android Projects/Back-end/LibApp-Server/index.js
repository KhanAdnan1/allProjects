const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
async function connectToMongoDB() {
  try {
    await mongoose.connect('mongodb+srv://akbproduct123:akbproduct123@cluster0.xnpbsqm.mongodb.net/library', {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('Connected to MongoDB Atlas');
  } catch (error) {
    console.error('Error connecting to MongoDB:', error);
  }
}
connectToMongoDB();
const studentSchema = new mongoose.Schema({
  clas: String,
  stuName: String,
  user: String,
  password: String,
});
const Students = mongoose.model('Students', studentSchema);
const booksSchema = new mongoose.Schema({
  clas: String,
  title: String,
  isbn: String,
  file: {
    data: Buffer,
    contentType: String,
  },
});
const Books = mongoose.model('Books', booksSchema);
const app = express();
const port = 5000;
app.use(bodyParser.json());
const novelsSchema=new mongoose.Schema({
  title:String,
  author:String,
  isbn:String,
  file:{
    data:Buffer,
    contentType:String,
  }
});
const Novels=mongoose.model('Nowels',novelsSchema);

const imageSchema=new mongoose.Schema({
  img:String
})
const Image= mongoose.model('Image',imageSchema);

const noticeSchema= new mongoose.Schema({
  notices:String

})
const Notice=mongoose.model('Notices',noticeSchema);

app.post('/login', async (req, res) => {
  const { user, password } = req.body;

  try {
    // Check if the user exists in the database
    const student = await Students.findOne({ user });
    if (!student) {
      // User not found
      return res.status(404).json({ error: 'Invalid username' });
    }
    // Compare the provided password with the stored hashed password
    const isPasswordValid = await bcrypt.compare(password, student.password);
    if (!isPasswordValid) {
      // Password is incorrect
      return res.status(401).json({ error: 'Invalid password' });
    }
    // Generate a JSON web token (JWT)
    const token = jwt.sign({ id: student._id }, 'your-secret-key');
    const className = student.clas;
    const stuName=student.stuName;
    const userName=user;
    return res.json({ token, className,stuName,userName });
  } catch (error) {
    console.error('Error logging in:', error);
    res.status(500).json({ error: 'An error occurred while logging in' });
  }
});

app.get('/books/:class/pdf', async (req, res) => {
  const className = req.params.class;
  try {
    const books = await Books.find({ clas: className });
    
    if (books.length === 0) {
      return res.status(404).json({ error: 'No books found for the given class' });
    }
    const pdfBooks = books.map(book => {
      const pdfData = Array.from(book.file.data); // Convert Buffer to Array
      const contentType = 'application/pdf';
      const title = book.title;
      return { title, pdfData, contentType };
    });
    res.json(pdfBooks);
  } catch (error) {
    console.error('Error fetching books:', error);
    res.status(500).json({ error: 'An error occurred while fetching the books' });
  }
});

//Novels
app.get('/novels/:pdf', async(req,res)=>{
  try{
    const novelsData= await Novels.find()
    if(novelsData.length ===0){
      return res.status(404).json({error:'Book not found'});
    }
    const novelsPDF=novelsData.map(novel =>{
      const novelPdfData=Array.from(novel.file.data);
      
      const contentType = 'application/json';
      const title=novel.title;
      return{title,novelPdfData,contentType};
    })
    res.json(novelsPDF);
  }catch(error){
    console.log('Error fetching novels:', error);
    res.status(500).json({ error: 'An error occurred while fetching the novels' });
  }
})

app.get('/images', async (req, res) => {
  try {
    Image.find({}).then(data => {
      //console.log(data); // Log the data to verify it's correct
      res.send({ status: 'ok', data: data });
    });
  } catch (error) {
    console.log(error);
    res.status(500).send({ status: 'error', message: 'Internal server error' });
  }
});

app.get('/notices', async (req, res) => {
  try {
    const noticeData = await Notice.find().select('notices'); // Select only the "notices" field
    res.json(noticeData);
  } catch (error) {
    res.status(500).json({ error: "An error occurred" });
  }
});


//......Forgot Password
app.post('/forgotpassword',async (req,res) =>{
  const {user,password}=req.body;
  try{
      const userId=await Students.findOne({user});
      console.log(userId);
      if(!userId){
        return res.status(404).json({error:'Invalid User name'});

      }
      const saltRounds = 10;
      const hashedPassword= await bcrypt.hash(password,saltRounds);
      await Students.updateOne({ user }, { password:hashedPassword });
      return res.status(200).json({ message: 'Password changed successfully' });
  }catch(error){
    console.log("User Not found");
  }

})


app.listen(port, () => {
  console.log('Server running on port:', port);
});
